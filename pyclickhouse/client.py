from abc import ABC, abstractmethod
from typing import Any, Iterable, Literal, Self, Sequence, cast

from asynch import Connection, Cursor
from clickhouse_connect import create_client
from clickhouse_connect.driver.asyncclient import AsyncClient

from .admin import Admin


def create_http_client(url: str, **kwargs: Any) -> AsyncClient:
    return AsyncClient(client=create_client(dsn=url, **kwargs))


def create_native_client(url: str, **kwargs: Any) -> Connection:
    return Connection(dsn=url, **kwargs)


class QueryResult:
    def __init__(
        self,
        columns: dict[str, str],
        rows: list[tuple[Any, ...]],
    ) -> None:
        self.columns = columns
        self.rows = rows

    def values(self) -> list[Any]:
        return list(item for row in self.rows for item in row)


class Client(ABC):
    @abstractmethod
    async def connect(self) -> None: ...

    @abstractmethod
    async def close(self) -> None: ...

    @abstractmethod
    async def ping(self) -> bool: ...

    @property
    @abstractmethod
    def database(self) -> str: ...

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
        *,
        columns: Iterable[str] = "*",
    ) -> int: ...

    @abstractmethod
    async def query(
        self,
        query: str,
        args: dict[str, Any] | None = None,
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

    def admin(
        self,
        database: str | None = None,
        cluster: str | None = None,
    ) -> Admin:
        return Admin(self, database=database or self.database, cluster=cluster)


class HttpClient(Client):
    _client: AsyncClient | None = None

    def __init__(self, url: str, **kwargs: Any):
        self.url = url
        self.options = kwargs

    @property
    def client(self) -> AsyncClient:
        if self._client is None:
            self._client = create_http_client(self.url, **self.options)
        return self._client

    async def connect(self) -> None:
        assert self.client is not None

    async def close(self) -> None:
        await self.client.close()

    async def ping(self) -> bool:
        return await self.client.ping()

    @property
    def database(self) -> str:
        return self.client.client.database or "__default__"

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
        *,
        columns: Iterable[str] = "*",
    ) -> int:
        rows = [list(row.values()) for row in data]
        result = await self.client.insert(table, data=rows, column_names=columns)
        return result.written_rows

    async def query(
        self,
        query: str,
        args: dict[str, Any] | None = None,
    ) -> QueryResult:
        result = await self.client.query(
            query=query,
            parameters=args,
        )
        column_names = result.column_names
        column_types = tuple(map(lambda c: c.name, result.column_types))
        rows = list(tuple(row) for row in result.result_rows)
        return QueryResult(rows=rows, columns=dict(zip(column_names, column_types)))


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

    @property
    def database(self) -> str:
        return self.client.database

    async def execute(
        self,
        query: str,
        args: Any = None,
        context: Any = None,
    ) -> Cursor:
        cursor = self.client.cursor()
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
        *,
        columns: Iterable[str] = "*",
    ) -> int:
        query = f"INSERT INTO {table} ({columns}) VALUES"
        rows = data
        cursor = await self.execute(query, args=rows)
        return cursor.rowcount

    async def query(
        self,
        query: str,
        args: dict[str, Any] | None = None,
    ) -> QueryResult:
        cursor = await self.execute(query, args)
        column_names = cast(tuple[str, ...], cursor._columns)
        column_types = cast(tuple[str, ...], cursor._types)
        rows = cast(list[tuple[Any, ...]], await cursor.fetchall())
        return QueryResult(rows=rows, columns=dict(zip(column_names, column_types)))


def get_client(
    url: str,
    *,
    mode: Literal["native", "http"] = "native",
    **kwargs: Any,
) -> Client:
    if mode == "http":
        return HttpClient(url=url, **kwargs)
    return NativeClient(url=url, **kwargs)
