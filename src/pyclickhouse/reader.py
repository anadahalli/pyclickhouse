from typing import TYPE_CHECKING, Any, AsyncGenerator, Sequence

from clickhouse_connect.driver.common import StreamContext
from clickhouse_connect.driver.query import QueryContext, QueryResult
from pydantic import BaseModel

from pyclickhouse.query import Query
from pyclickhouse.table import Table
from pyclickhouse.view import View

if TYPE_CHECKING:
    from pyclickhouse.client import Client


type Select = str | Query | Table | View
type Parameters[R] = R | dict[str, Any] | None
type Data[T] = T | dict[str, Any]
type DataStream = AsyncGenerator[Data, None]


class ReaderError(Exception):
    """Raised when a reader encounters an error."""

    pass


class Reader[T: BaseModel, R: BaseModel]:
    """Reads data from the ClickHouse database using a given query."""

    select: Select
    model: type[T] | None
    parameters: type[R] | None
    _client: Client | None
    _context: QueryContext | None

    def __init__(
        self,
        select: Select,
        *,
        client: Client | None = None,
        model: type[T] | None = None,
        parameters: type[R] | None = None,
        max_block_size: int = 65536,
        settings: dict[str, Any] | None = None,
        transport_settings: dict[str, str] | None = None,
    ) -> None:
        """
        Initializes a new Reader instance.

        Args:
            client: The ClickHouse client to use.
            select: The query to execute.
            model: Optional model to use for the response data.
            parameters: Optional model to use for validating parameters.
            max_block_size: The maximum block size to use for streaming. Defaults to 65536.
            settings: The settings to use for the insert. Defaults to None.
            transport_settings: The transport settings to use for the insert. Defaults to None.
        """

        self.select = select
        self.model = model
        self.parameters = parameters
        self.max_block_size = max_block_size
        self.settings = settings
        self.transport_settings = transport_settings

        self._client = client
        self._context = None

        self._read_rows: int = 0

    @property
    def read_rows(self) -> int:
        """Returns the number of rows read from the database."""
        return self._read_rows

    def bind(self, client: Client) -> None:
        if self._client is not None:
            raise ReaderError("Client is already set")
        self._client = client

    def _create_context(self, client: Client) -> QueryContext:
        return client.create_query_context(
            query=self._get_query_string(self.select),
            parameters={},
            settings=self.settings,
            transport_settings=self.transport_settings,
        )

    def _get_query_string(self, select: Select) -> str:
        if isinstance(select, Table):
            return Query(select).compile()

        if isinstance(select, View):
            if select.table:
                return Query(select.table).compile()
            return Query(select.get_name()).compile()

        if isinstance(select, Query):
            return select.compile()

        return str(select)

    def _deserialize_row(self, data: Data) -> Data:
        if self.model:
            return self.model.model_validate(data)
        return data

    def _deserialize_block(self, data: Sequence[Data]) -> Sequence[Data]:
        if self.model:
            return [self.model.model_validate(row) for row in data]
        return data

    def _validate_parameters(self, parameters: Parameters) -> Parameters:
        if parameters is None:
            return None

        if isinstance(parameters, BaseModel):
            if self.parameters and not isinstance(parameters, self.parameters):
                raise TypeError(
                    f"Invalid parameters type, not an instance of {type(self.parameters)}"
                )
            return parameters.model_dump()

        return parameters

    async def _query(self, parameters: Parameters = None) -> QueryResult:
        if self._client is None:
            raise ReaderError("Client is not set")

        if self._context is None:
            self._context = self._create_context(self._client)

        return await self._client.query(
            context=self._context,
            parameters=parameters,
        )

    async def _query_stream(self, parameters: Parameters = None) -> StreamContext:
        if self._client is None:
            raise ReaderError("Client is not set")

        if self._context is None:
            self._context = self._create_context(self._client)

        return await self._client.query_row_block_stream(
            context=self._context,
            parameters=parameters,
        )

    async def _stream_generator(self, result: StreamContext) -> DataStream:
        column_names = getattr(result.source, "column_names")
        async with result:
            async for block in result:
                for row in block:
                    data = dict(zip(column_names, row))
                    item = self._deserialize_row(data)
                    self._read_rows += 1
                    yield item

    async def _result_generator(self, result: QueryResult) -> Sequence[Data]:
        data = result.named_results()
        items = [self._deserialize_row(row) for row in data]
        self._read_rows += len(items)
        return items

    async def query(self, parameters: Parameters = None) -> Sequence[Data]:
        """Executes the query and returns the results as a QueryResult."""
        parameters = self._validate_parameters(parameters)
        result = await self._query(parameters=parameters)
        return await self._result_generator(result)

    async def stream(self, parameters: Parameters = None) -> DataStream:
        # async def query(self, parameters: Parameters = None) -> Stream:
        """Executes the query and returns an AsyncGenerator"""
        parameters = self._validate_parameters(parameters)
        result = await self._query_stream(parameters)
        return self._stream_generator(result)
