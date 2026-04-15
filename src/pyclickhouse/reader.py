from typing import TYPE_CHECKING, Any, AsyncGenerator

from clickhouse_connect.driver.common import StreamContext
from clickhouse_connect.driver.query import QueryContext, QueryResult
from pydantic import BaseModel

from pyclickhouse.query import Query
from pyclickhouse.table import Table
from pyclickhouse.view import View

if TYPE_CHECKING:
    from pyclickhouse.client import Client


class Reader[T: BaseModel, R: BaseModel]:
    """Reads data from the ClickHouse database using a given query."""

    client: Client
    select: str | Query | Table | View
    model: type[T] | None
    parameters: type[R] | None
    context: QueryContext | None

    def __init__(
        self,
        client: Client,
        select: str | Query | Table | View,
        *,
        model: type[T] | None = None,
        parameters: type[R] | None = None,
        stream: bool = True,
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
            stream: Whether to stream the results. Defaults to True.
            max_block_size: The maximum block size to use for streaming. Defaults to 65536.
            settings: The settings to use for the insert. Defaults to None.
            transport_settings: The transport settings to use for the insert. Defaults to None.
        """

        self.client = client
        self.select = select
        self.model = model
        self.parameters = parameters
        self.stream = stream
        self.max_block_size = max_block_size
        self.settings = settings
        self.transport_settings = transport_settings

        self._read_rows: int = 0
        self.context = None

    @property
    def read_rows(self) -> int:
        """Returns the number of rows read from the database."""
        return self._read_rows

    def _create_context(self) -> QueryContext:
        return self.client.create_query_context(
            query=self._get_query_string(self.select),
            parameters={},
            settings=self.settings,
            transport_settings=self.transport_settings,
        )

    def _get_query_string(self, select: str | Query | Table | View) -> str:
        if isinstance(select, Table):
            return Query(select).compile()

        if isinstance(select, View):
            if select.table:
                return Query(select.table).compile()
            return Query(select.get_name()).compile()

        if isinstance(select, Query):
            return select.compile()

        return select

    def _deserialize(self, data: dict[str, Any]) -> T | dict:
        if self.model:
            return self.model.model_validate(data)
        return data

    async def _query(
        self,
        parameters: dict[str, Any] | None = None,
    ) -> QueryResult | StreamContext:
        if self.context is None:
            self.context = self._create_context()

        if self.stream:
            return await self.client.query_row_block_stream(
                context=self.context,
                parameters=parameters,
            )

        return await self.client.query(
            context=self.context,
            parameters=parameters,
        )

    async def query(
        self,
        parameters: R | dict[str, Any] | None = None,
    ) -> AsyncGenerator[T | dict[str, Any], None]:
        """
        Executes the query and returns the results as a list of models or dicts.
        """
        if isinstance(parameters, BaseModel):
            if self.parameters and not isinstance(parameters, self.parameters):
                raise TypeError(
                    f"Invalid parameters type, not an instance of {type(self.parameters)}"
                )
            parameters = parameters.model_dump()

        result = await self._query(parameters)

        if isinstance(result, StreamContext):
            column_names = getattr(result.source, "column_names")
            with result:
                for block in result:
                    for row in block:
                        data = dict(zip(column_names, row))
                        item = self._deserialize(data)
                        self._read_rows += 1
                        yield item

        else:
            block = result.named_results()
            for row in block:
                item = self._deserialize(row)
                self._read_rows += 1
                yield item

    # async def _get_response_model(self) -> type[BaseModel]:
    #     if isinstance(self.select, Table):
    #         return self.select.get_model()

    #     elif isinstance(self.select, View):
    #         if self.select.table:
    #             return self.select.table.get_model()
    #         else:
    #             table = await self.client.admin().get_table(self.select.get_name())
    #             return table.get_model()
    #     elif isinstance(self.select, Query):
    #         model = await self.client.admin().create_model(self.select, "Response")
    #         return model
    #     else:
    #         raise TypeError(f"Unsupported type for select: {type(self.select)}")
