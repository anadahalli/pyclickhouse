from abc import ABC, abstractmethod
from typing import Any, Iterable, Literal, Self, Sequence, cast

from asynch import Connection, Cursor
from clickhouse_connect import create_client
from clickhouse_connect.driver.asyncclient import AsyncClient
from pydantic import BaseModel

from .admin import Admin
from .query import Query
from .reader import Reader
from .table import Table
from .utils import clean_query_param_types
from .writer import Writer


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

    def items(self) -> list[dict[str, Any]]:
        column_names = self.columns.keys()
        return [dict(zip(column_names, row)) for row in self.rows]

    def first(self) -> Any:
        if rows := self.rows:
            if row := rows[0]:
                return row[0]
        return None


class Client(ABC):
    """
    A ClickHouse client that provides asynchronous database operations.
    """

    @abstractmethod
    async def connect(self) -> None:
        """Connect to the ClickHouse database."""
        ...

    @abstractmethod
    async def close(self) -> None:
        """Close the connection to the ClickHouse database."""
        ...

    @abstractmethod
    async def ping(self) -> bool:
        """Ping the ClickHouse database to check if the connection is alive."""
        ...

    @property
    @abstractmethod
    def database(self) -> str:
        """Get the name of the current database."""
        ...

    @abstractmethod
    async def command(
        self,
        query: str,
        args: Any | None = None,
        context: Any | None = None,
    ) -> bool:
        """
        Execute a command on the ClickHouse database.

        Args:
            query: The SQL command to execute.
            args: Optional arguments to pass to the command.
            context: Optional context to pass to the command.

        Returns:
            True if the command was executed successfully, False otherwise.

        Raises:
            Exception: If the command execution fails.

        """
        ...

    @abstractmethod
    async def insert(
        self,
        table: str,
        data: Sequence[Sequence[Any]],
        *,
        columns: Iterable[str] = "*",
        database: str | None = None,
        **kwargs: Any,
    ) -> int:
        """
        Insert data into a table.

        Args:
            table: The name of the table to insert into.
            data: The data to insert.
            columns: Optional columns to insert into.
            database: Optional database to insert into.
            **kwargs: Optional keyword arguments to pass to the insert operation.

        Returns:
            The number of rows inserted.

        Raises:
            Exception: If the insert operation fails.

        """
        ...

    @abstractmethod
    async def query(
        self,
        query: str,
        args: dict[str, Any] | None = None,
    ) -> QueryResult:
        """
        Execute a query on the ClickHouse database.

        Args:
            query: The SQL query to execute.
            args: Optional arguments to pass to the query.

        Returns:
            The result of the query.

        Raises:
            Exception: If the query execution fails.

        """
        ...

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
        """
        Return an Admin instance for the given database and cluster.

        Args:
            database: Optional database to use.
            cluster: Optional cluster to use.

        Returns:
            An Admin instance.
        """
        return Admin(
            client=self,
            database=database or self.database,
            cluster=cluster,
        )

    def writer(
        self,
        table: Table,
        *,
        batch: bool = True,
        batch_size: int = 1000,
        database: str | None = None,
    ) -> Writer:
        """
        Return a Writer instance for the given table.

        Args:
            table: The table to write to.
            batch: Whether to use batch inserts.
            batch_size: The batch size to use for inserts.
            database: Optional database to use.

        Returns:
            A Writer instance.
        """
        return Writer(
            client=self,
            table=table,
            batch=batch,
            batch_size=batch_size,
            database=database,
        )

    def reader(
        self,
        query: Query,
        *,
        args_model: type[BaseModel] | None = None,
        response_model: type[BaseModel] | None = None,
        database: str | None = None,
    ) -> Reader:
        """
        Return a Reader instance for the given query.

        Args:
            query: The query to read from.
            args_model: Optional model for query arguments.
            response_model: Optional model for query response.
            database: Optional database to use.

        Returns:
            A Reader instance.
        """
        return Reader(
            client=self,
            query=query,
            args_model=args_model,
            response_model=response_model,
            database=database,
        )


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
        data: Sequence[Sequence[Any]],
        *,
        columns: Iterable[str] = "*",
        database: str | None = None,
        **kwargs: Any,
    ) -> int:
        table_name = f"{database or self.database}.{table}"
        result = await self.client.insert(
            table=table_name,
            data=data,
            column_names=columns,
            database=database,
            **kwargs,
        )
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
        data: Sequence[Sequence[Any]],
        *,
        columns: Iterable[str] = "*",
        database: str | None = None,
        **kwargs: Any,
    ) -> int:
        table_name = f"{database or self.database}.{table}"
        table_columns = ", ".join(columns) if columns != "*" else columns
        query = f"INSERT INTO {table_name} ({table_columns}) VALUES"
        cursor = await self.execute(query, args=data)
        return cursor.rowcount

    async def query(
        self,
        query: str,
        args: dict[str, Any] | None = None,
    ) -> QueryResult:
        query = clean_query_param_types(query)
        cursor = await self.execute(query, args)
        column_names = cast(tuple[str, ...], cursor._columns)
        column_types = cast(tuple[str, ...], cursor._types)
        rows = cast(list[tuple[Any, ...]], await cursor.fetchall())
        return QueryResult(rows=rows, columns=dict(zip(column_names, column_types)))


def get_client(
    url: str,
    *,
    mode: Literal["native", "http"] = "http",
    **kwargs: Any,
) -> Client:
    """
    Get a ClickHouse client for the given URL and mode.

    Args:
        url: The URL of the ClickHouse server.
        mode: The mode of the client, either "native" or "http".
        **kwargs: Additional keyword arguments for the client.

    Returns:
        A ClickHouse client.
    """
    if mode == "http":
        return HttpClient(url=url, **kwargs)
    return NativeClient(url=url, **kwargs)
