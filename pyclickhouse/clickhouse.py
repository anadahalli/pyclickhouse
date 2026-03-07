from typing import Any, Self, cast

from asynch import Connection, DictCursor
from pydantic import BaseModel

from .query import Query
from .table import Table, create_result_model


class ModelCursor(DictCursor):
    @property
    def rowcount(self) -> int:
        return self._rowcount

    @property
    def columns(self) -> list[tuple[str, str]]:
        return cast(list[tuple[str, str]], self._columns_with_types)


class ModelWriter[W: BaseModel]:
    def __init__(self, table: Table, *, batch: bool = True) -> None:
        self.table = table
        self.batch = batch

    def insert(self, data: BaseModel) -> None:
        pass

    def __await__(self) -> None:
        pass


class ModelResult[R: BaseModel]:
    def __init__(
        self,
        cursor: ModelCursor,
        model: type[R] | None = None,
    ) -> None:
        self._cursor = cursor
        self._model = model or create_result_model(cursor.columns)

    def _validate(self, data: dict) -> R:
        # use pydantic type adapter
        return cast(R, self._model.model_validate(data))

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> R:
        while True:
            one = await self._cursor.fetchone()
            if not one:
                raise StopAsyncIteration
            return self._validate(one)


class ClickHouse(Connection):
    def __init__(self, url: str, **options: Any):
        super().__init__(dsn=url, **options)

    def model_cursor(self) -> ModelCursor:
        return ModelCursor(self, self.echo)

    async def execute(
        self,
        query: str,
        args: Any = None,
        context: Any = None,
    ) -> ModelCursor:
        cursor = self.model_cursor()
        async with cursor:
            await cursor.execute(query, args, context)
        return cursor

    async def create_table(self, table: Table, database: str | None = None) -> bool:
        query = f"CREATE TABLE {table.to_create_sql(database or self.database)}"
        result = await self.execute(query)
        return bool(result.rowcount)

    async def drop_table(self, table: Table | str, database: str | None = None) -> bool:
        table_name = table._name if isinstance(table, Table) else table
        query = f"DROP TABLE {database or self.database}.{table_name}"
        result = await self.execute(query)
        return bool(result.rowcount)

    async def show_tables(self) -> list[str]:
        result = await self.execute(f"SHOW TABLES FROM {self.database}")
        return [res["name"] for res in await result.fetchall()]

    async def get_table(self, name: str) -> Table:
        result = await self.execute(f"DESC TABLE {self.database}.{name}")
        columns = await result.fetchall()
        query = f"SELECT engine_full FROM system.tables WHERE database = '{self.database}' AND table = '{name}'"
        result = await self.execute(query)
        engine_full = await result.fetchone()
        engine = engine_full.get("engine_full", "")
        return Table.from_sql(name=name, engine_sql=engine, columns_sql=columns)

    async def insert(
        self,
        data: BaseModel,
        *,
        table: Table | None = None,
        database: str | None = None,
    ) -> int:
        table = table or Table.from_model(type(data))
        query = f"INSERT INTO {table.to_insert_sql(database or self.database)}"
        args = data.model_dump()
        result = await self.execute(query, args=[args])
        return result.rowcount

    async def query[R: BaseModel](
        self,
        query: Query | str,
        *,
        model: type[R] | None = None,
    ) -> ModelResult[R]:
        query = str(query) if isinstance(query, Query) else query
        cursor = await self.execute(query)
        return ModelResult(cursor, model)
