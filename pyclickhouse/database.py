import logging
from typing import Any, Self

from asynch import Connection, Cursor, DictCursor
from pydantic import BaseModel

from .query import Query, create_result_model
from .registry import Registry, default_registry
from .table import Table

logger = logging.getLogger(__name__)


class Database:
    """Connect to a ClickHouse database.

    Args:
        url (str): The URL of the ClickHouse database.
        **options (Any): Additional options for the ClickHouse database connection.

    Examples:
        >>> db = Database("http://localhost:8123")
        >>> await db.ping()
    """

    def __init__(self, url: str, **options: Any) -> None:
        self.url = url
        self.options = options
        self.connection = Connection(dsn=url, **options)

    async def __aenter__(self) -> Self:
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    async def connect(self) -> None:
        await self.connection.connect()

    async def close(self) -> None:
        await self.connection.close()

    @property
    def status(self) -> str:
        return self.connection.status

    def cursor(self, dict_mode: bool = True) -> Cursor:
        if dict_mode:
            return self.connection.cursor(cursor=DictCursor)
        return self.connection.cursor()

    async def ping(self) -> None:
        await self.connection.ping()

    async def execute(
        self,
        query: str,
        args: list[dict] | None = None,
        dict_mode: bool = True,
    ) -> Cursor:
        cursor = self.cursor(dict_mode=dict_mode)
        async with cursor:
            await cursor.execute(query, args)
        return cursor

    async def command(self, query: str) -> bool:
        cursor = await self.execute(query, dict_mode=False)
        return bool(cursor.rowcount or 0)

    async def create_database(self, name: str | None = None) -> None:
        database: str = name or self.connection.database
        sql = f"CREATE DATABASE IF NOT EXISTS {database}"
        await self.execute(sql)

    async def drop_database(self, name: str | None = None) -> None:
        database: str = name or self.connection.database
        sql = f"DROP DATABASE IF EXISTS {database}"
        await self.execute(sql)

    async def create_table(self, table: type[Table]) -> bool:
        return await self.command(table.to_create_sql())

    async def drop_table(self, table: type[Table]) -> bool:
        sql = f"DROP TABLE IF EXISTS {table.get_table_name()}"
        return await self.command(sql)

    async def list_tables(self) -> list[str]:
        cursor = await self.execute("SHOW TABLES")
        return [val.get("name") for val in await cursor.fetchall()]

    async def describe_table(self, table: type[Table]) -> list[dict]:
        sql = f"DESCRIBE TABLE {table.get_table_name()}"
        cursor = await self.execute(sql)
        return await cursor.fetchall()

    async def attach_table(self, table: type[Table]) -> None:
        sql = f"ATTACH TABLE {table.table_config.name}"
        await self.execute(sql)

    async def detach_table(self, table: type[Table]) -> None:
        sql = f"DETACH TABLE {table.table_config.name}"
        await self.execute(sql)

    async def create_view(self) -> None:
        pass

    async def drop_view(self) -> None:
        pass

    async def create_all(self, registry: Registry = default_registry) -> None:
        for table in registry.tables.values():
            await self.create_table(table)

    async def insert(
        self,
        item: Table,
    ) -> bool:
        query = item.to_insert_sql()
        data: dict[str, Any] = item.model_dump()
        result = await self.execute(query, args=[data])
        return bool(result.rowcount)

    async def query(
        self,
        query: str | Query,
        *,
        model: bool = True,
    ) -> list[BaseModel] | list[dict[str, Any]]:
        query = str(query)
        result = await self.execute(query)
        items = await result.fetchall()

        if not model:
            return list(items)

        model_cls = create_result_model(
            name="Result", columns=result._columns_with_types
        )
        return [model_cls.model_validate(data) for data in items]
