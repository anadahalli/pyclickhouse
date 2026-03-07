from pydantic import BaseModel

from pyclickhouse.clickhouse import ClickHouse, ModelResult
from pyclickhouse.engines import Memory, MergeTree
from pyclickhouse.query import Query
from pyclickhouse.table import table

from .container import ClickHouseContainer


class TestClickHouse:
    async def test_connection(self, clickhouse: ClickHouseContainer) -> None:
        url = clickhouse.get_url()
        async with ClickHouse(url) as db:
            await db.ping()

    async def test_table_operations(self, clickhouse: ClickHouseContainer) -> None:
        db = ClickHouse(clickhouse.get_url())

        class Model(BaseModel):
            name: str
            value: int

        model = table(
            Model,
            name="test",
            engine=MergeTree(order_by="name"),
        )

        async with db:
            assert await db.show_tables() == []

            assert await db.create_table(model)
            assert await db.show_tables() == ["test"]

            dtable = await db.get_table(model._name)
            assert dtable._columns == model._columns

            assert await db.drop_table(model)
            assert await db.show_tables() == []

    async def test_table_insert(self, clickhouse: ClickHouseContainer) -> None:
        db = ClickHouse(clickhouse.get_url(), echo=True)

        class Data(BaseModel):
            key: str
            val: int

        async with db:
            data = Data(key="one", val=1)

            model = table(Data)
            assert await db.create_table(model)
            assert await db.insert(data) == 1
            result = await db.execute(f"SELECT * FROM {model._name}")
            assert await result.fetchone() == data.model_dump()

            model = table(Data, name="new")
            assert await db.create_table(model)
            assert await db.insert(data, table=model) == 1
            result = await db.execute(f"SELECT * FROM {model._name}")
            assert await result.fetchone() == data.model_dump()

    async def test_table_query(self, clickhouse: ClickHouseContainer) -> None:
        db = ClickHouse(clickhouse.get_url())

        class Store(BaseModel):
            key: str
            val: int

        class Result(BaseModel):
            key: str
            val: int

        model = table(Store, engine=Memory())

        async with db:
            assert await db.create_table(model)

            assert await db.insert(Store(key="one", val=1)) == 1
            assert await db.insert(Store(key="two", val=2)) == 1
            assert await db.insert(Store(key="three", val=3)) == 1
            assert await db.insert(Store(key="four", val=4)) == 1

            query = Query(model).sort(model.val)

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
