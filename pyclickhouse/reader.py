from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, create_model

from .query import Query

if TYPE_CHECKING:
    from .client import Client, QueryResult


class Reader:
    _client: Client
    _query: Query

    def __init__(
        self,
        client: Client,
        query: Query,
        *,
        args_model: type[BaseModel] | None = None,
        response_model: type[BaseModel] | None = None,
        database: str | None = None,
    ) -> None:
        self._client = client
        self._query = query
        self._args_model = args_model
        self._response_model = response_model
        self._database = database
        self._count: int = 0

    @property
    def read_rows(self) -> int:
        return self._count

    def _get_model(self, columns: dict[str, str]) -> type[BaseModel]:
        if self._response_model is None:
            fields = {}
            return create_model("Response", **fields)
        return self._response_model

    def _deserialize(
        self, row: tuple[Any, ...], columns: dict[str, str]
    ) -> BaseModel | dict:
        data = dict(zip(columns.keys(), row))
        if self._response_model:
            return self._response_model.model_validate(data)
        return data

    def _to_model(self, result: QueryResult) -> list[BaseModel | dict]:
        return [self._deserialize(row, result.columns) for row in result.rows]

    async def _execute(
        self,
        query: str,
        args: dict[str, Any] | None = None,
    ) -> QueryResult:
        return await self._client.query(query, args)

    async def query(
        self,
        args: BaseModel | dict[str, Any] | None = None,
        skip: int | None = None,
        limit: int | None = None,
    ) -> list[BaseModel | dict]:
        query = self._query

        if skip is not None or limit is not None:
            start, end = None, None
            if limit is not None:
                assert isinstance(limit, int)
                end = skip + limit if skip is not None else limit
            if skip is not None:
                assert isinstance(skip, int)
                start = skip + 1
            query = query.take(start=start, end=end)

        sql = query.compile()

        query_args: dict[str, Any] | None = None
        if args:
            if isinstance(args, BaseModel):
                if self._args_model and not isinstance(args, self._args_model):
                    args_model = self._args_model.__name__
                    raise TypeError(
                        f"Invalid args type, not an instance of {args_model}"
                    )
                query_args = args.model_dump()
            else:
                query_args = args

        result = await self._execute(query=sql, args=query_args)
        items = self._to_model(result)

        self._count += len(items)
        return items
