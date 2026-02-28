from typing import Any, Self

from asynch import Connection, Cursor, DictCursor

from .table import Table


class Database:
    def __init__(self, url: str, **options: Any) -> None:
        self.url = url
        self.options = options
        self.connection = Connection(dsn=url, **options)
        self.tables: dict[str, type[Table]] = {}

    async def __aenter__(self) -> Self:
        await self.connection.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.connection.close()

    def cursor(self) -> Cursor:
        return self.connection.cursor(cursor=DictCursor)

    async def execute(self, sql: str, args: list[dict] | None = None) -> int | None:
        async with self.cursor() as cursor:
            return await cursor.execute(sql, args)

    async def ping(self) -> None:
        await self.connection.ping()

    async def create_database(self, name: str | None = None) -> None:
        database: str = name or self.connection.database
        sql = f"CREATE DATABASE IF NOT EXISTS {database}"
        await self.execute(sql)

    async def drop_database(self, name: str | None = None) -> None:
        database: str = name or self.connection.database
        sql = f"DROP DATABASE IF EXISTS {database}"
        await self.execute(sql)

    async def create_table(self, table: type[Table]) -> None:
        sql = table.to_create_sql()
        await self.execute(sql)

    async def drop_table(self, table: type[Table]) -> None:
        sql = f"DROP TABLE IF EXISTS {table.table_config.name}"
        await self.execute(sql)

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

    async def insert(
        self,
        item: Table,
    ) -> int:
        sql = item.to_insert_sql()
        data: dict[str, Any] = item.model_dump()
        result = await self.execute(sql, args=[data])
        return result or 0

    async def query(
        self,
        sql: str,
        model: type[Table] | None = None,
    ) -> None:
        pass

    def register_table(self, table: type[Table]) -> None:
        self.tables[table.get_table_name()] = table
