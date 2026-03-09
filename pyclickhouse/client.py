from abc import ABC, abstractmethod
from typing import Any, Iterable, Literal, Self, Sequence, cast

from asynch import Connection, Cursor, DictCursor
from clickhouse_connect import create_client
from clickhouse_connect.driver.asyncclient import AsyncClient


def create_http_client(url: str, **kwargs: Any) -> AsyncClient:
    return AsyncClient(client=create_client(dsn=url, **kwargs))


def create_native_client(url: str, **kwargs: Any) -> Connection:
    return Connection(dsn=url, **kwargs)


class QuerySummary:
    def __init__(self, row_count: int, summary: dict[str, Any] = {}) -> None:
        self.row_count = row_count
        self.summary = summary


class QueryResult:
    def __init__(
        self,
        column_names: tuple[str, ...],
        column_types: tuple[str, ...],
        rows: list[dict[str, Any]],
    ) -> None:
        self.column_names = column_names
        self.column_types = column_types
        self.rows = rows


class Client(ABC):
    @abstractmethod
    async def connect(self) -> None: ...

    @abstractmethod
    async def close(self) -> None: ...

    @abstractmethod
    async def ping(self) -> bool: ...

    @abstractmethod
    async def command(
        self,
        query: str,
        args: Any | None = None,
        context: Any | None = None,
    ) -> bool: ...

    @abstractmethod
    async def insert(
        self,
        table: str,
        data: Sequence[dict[str, Any]],
        columns: Iterable[str] = "*",
    ) -> QuerySummary: ...

    @abstractmethod
    async def query(
        self,
        query: str,
        args: Any | None = None,
    ) -> QueryResult: ...

    async def __aenter__(self) -> Self:
        await self.connect()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> None:
        await self.close()


class HttpClient(Client):
    client: AsyncClient

    def __init__(self, url: str, **kwargs: Any):
        self.url = url
        self.options = kwargs
        self.client = create_http_client(url, **kwargs)

    async def connect(self) -> None:
        pass

    async def close(self) -> None:
        await self.client.close()

    async def ping(self) -> bool:
        return await self.client.ping()

    async def command(
        self,
        query: str,
        args: Any = None,
        context: Any = None,
    ) -> bool:
        await self.client.command(query, parameters=args)
        return True

    async def insert(
        self,
        table: str,
        data: Sequence[dict[str, Any]],
        columns: Iterable[str] = "*",
    ) -> QuerySummary:
        rows = [list(row.values()) for row in data]
        result = await self.client.insert(table, data=rows, column_names=columns)
        return QuerySummary(row_count=result.written_rows, summary=result.summary)

    async def query(
        self,
        query: str,
        args: Any = None,
    ) -> QueryResult:
        result = await self.client.query(
            query=query,
            parameters=args,
        )
        column_names = result.column_names
        column_types = tuple(map(lambda c: c.name, result.column_types))
        rows = list(result.named_results())
        return QueryResult(
            column_names=column_names,
            column_types=column_types,
            rows=rows,
        )


class NativeClient(Client):
    client: Connection

    def __init__(self, url: str, **kwargs: Any):
        self.url = url
        self.options = kwargs
        self.client = create_native_client(url, **kwargs)

    async def connect(self) -> None:
        await self.client.connect()

    async def close(self) -> None:
        await self.client.close()

    async def ping(self) -> bool:
        return await self.client._connection.ping()

    async def execute(
        self,
        query: str,
        args: Any = None,
        context: Any = None,
    ) -> Cursor:
        cursor = self.client.cursor(DictCursor)
        async with cursor:
            await cursor.execute(query, args, context)
        return cursor

    async def command(
        self,
        query: str,
        args: Any = None,
        context: Any = None,
    ) -> bool:
        await self.execute(query, args, context)
        return True

    async def insert(
        self,
        table: str,
        data: Sequence[dict[str, Any]],
        columns: Iterable[str] = "*",
    ) -> QuerySummary:
        query = f"INSERT INTO {table} ({columns}) VALUES"
        rows = data
        cursor = await self.execute(query, args=rows)
        row_count = cast(int, cursor._rowcount)
        return QuerySummary(row_count=row_count)

    async def query(
        self,
        query: str,
        args: Any = None,
    ) -> QueryResult:
        cursor = await self.execute(query, args)
        column_names = cast(tuple[str, ...], cursor._columns)
        column_types = cast(tuple[str, ...], cursor._types)
        rows = await cursor.fetchall()
        return QueryResult(
            column_names=column_names,
            column_types=column_types,
            rows=rows,
        )


def get_client(
    url: str,
    *,
    mode: Literal["native", "http"] = "native",
    **kwargs: Any,
) -> Client:
    if mode == "http":
        return HttpClient(url=url, **kwargs)
    return NativeClient(url=url, **kwargs)
