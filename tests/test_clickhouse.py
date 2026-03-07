from pydantic import BaseModel

from pyclickhouse.clickhouse import ClickHouse, ModelResult
from pyclickhouse.query import Query
from pyclickhouse.table import Table, TableConfig

from .container import ClickHouseContainer


class TestClickHouse:
    async def test_connection(self, clickhouse: ClickHouseContainer) -> None:
        url = clickhouse.get_url()
        async with ClickHouse(url) as db:
            await db.ping()

    async def test_table_operations(self, clickhouse: ClickHouseContainer) -> None:
        db = ClickHouse(clickhouse.get_url())

        class Model(BaseModel):
            key: str
            val: int

        table = Table.from_model(
            Model, config=TableConfig(engine="MergeTree", order_by="key")
        )

        async with db:
            assert await db.show_tables() == []

            assert await db.create_table(table)
            assert await db.show_tables() == ["model"]

            dtable = await db.get_table(table._table_name)
            assert dtable._table_columns == table._table_columns

            assert await db.drop_table(table)
            assert await db.show_tables() == []

    async def test_table_insert(self, clickhouse: ClickHouseContainer) -> None:
        db = ClickHouse(clickhouse.get_url(), echo=True)

        class Data(BaseModel):
            key: str
            val: int

        async with db:
            data = Data(key="one", val=1)

            table = Table.from_model(Data)
            assert await db.create_table(table)
            assert await db.insert(data) == 1
            result = await db.execute(f"SELECT * FROM {table._table_name}")
            assert await result.fetchone() == data.model_dump()

            table = Table.from_model(Data, name="new")
            assert await db.create_table(table)
            assert await db.insert(data, table=table) == 1
            result = await db.execute(f"SELECT * FROM {table._table_name}")
            assert await result.fetchone() == data.model_dump()

    async def test_table_query(self, clickhouse: ClickHouseContainer) -> None:
        db = ClickHouse(clickhouse.get_url())

        class Store(BaseModel):
            key: str
            val: int

        class Result(BaseModel):
            key: str
            val: int

        table = Table.from_model(Store)

        async with db:
            assert await db.create_table(table)

            assert await db.insert(Store(key="one", val=1)) == 1
            assert await db.insert(Store(key="two", val=2)) == 1
            assert await db.insert(Store(key="three", val=3)) == 1
            assert await db.insert(Store(key="four", val=4)) == 1

            query = Query(table).sort(table.val)

            result = await db.query(query, model=Store)
            assert isinstance(result, ModelResult)
            out = [r async for r in result]
            assert out == [
                Store(key="one", val=1),
                Store(key="two", val=2),
                Store(key="three", val=3),
                Store(key="four", val=4),
            ]

            result = await db.query(query)
            assert isinstance(result, ModelResult)
            out = await anext(result)
            assert out.key == "one"
            assert out.val == 1
