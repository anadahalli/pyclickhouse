from asynch.proto.models.enums import ConnectionStatus, CursorStatus
from pydantic import BaseModel

from pyclickhouse import Database, Query, Table

from .container import ClickHouseContainer


class TestDatabase:
    async def test_connection(self, clickhouse: ClickHouseContainer) -> None:
        url = clickhouse.get_url()

        # manaual
        db = Database(url)
        try:
            assert db.status == ConnectionStatus.created
            await db.connect()
            assert db.status == ConnectionStatus.opened
            await db.ping()
        finally:
            await db.close()
            assert db.status == ConnectionStatus.closed

        # context
        db = Database(url)
        assert db.status == ConnectionStatus.created
        async with db:
            assert db.status == ConnectionStatus.opened
            await db.ping()
        assert db.status == ConnectionStatus.closed

        # cursor
        db = Database(url)
        try:
            await db.connect()
            cursor = db.cursor()
            assert cursor.status == CursorStatus.ready
        finally:
            await cursor.close()
            assert cursor.status == CursorStatus.closed
            await db.close()

    async def test_cursor(self, clickhouse: ClickHouseContainer) -> None:
        async with Database(clickhouse.get_url()) as db:
            cursor = await db.execute("SELECT 1")
            assert cursor.rowcount == 1
            assert await cursor.fetchone() == {"1": 1}

    async def test_table_operations(self, clickhouse: ClickHouseContainer) -> None:
        class First(Table):
            key: str
            val: int

        class Second(Table):
            key: str
            val: int

        async with Database(clickhouse.get_url()) as db:
            assert await db.create_table(First)
            assert await db.create_table(Second)
            assert await db.list_tables() == ["first", "second"]
            # print(await db.describe_table(First))
            assert await db.drop_table(First)
            assert await db.drop_table(Second)
            assert await db.list_tables() == []

    async def test_pydantic_cursor(self) -> None:
        pass

    async def test_registry(self) -> None:
        pass

    async def test_insert(self, clickhouse: ClickHouseContainer) -> None:
        class Store(Table):
            key: str
            val: int

        async with Database(clickhouse.get_url(), echo=True) as db:
            assert await db.create_table(Store)
            data = Store(key="name", val=1)
            assert await db.insert(data)
            query = f"SELECT * FROM {Store.get_table_name()} WHERE key = 'name'"
            res = await db.execute(query)
            await res.fetchall() == data.model_dump()

    async def test_query(self, clickhouse: ClickHouseContainer) -> None:
        class Data(Table):
            key: str
            val: int

        async with Database(clickhouse.get_url(), echo=True) as db:
            assert await db.create_table(Data)
            data_1 = Data(key="first", val=1)
            data_2 = Data(key="second", val=2)
            assert await db.insert(data_1)
            assert await db.insert(data_2)

            # simple
            query = Query(Data).sort(Data.val)
            result = await db.query(query, model=False)
            assert result == [{"key": "first", "val": 1}, {"key": "second", "val": 2}]

            result = await db.query(query, model=True)
            first, second = result
            assert isinstance(first, BaseModel)
            assert isinstance(second, BaseModel)
            assert first.model_dump() == {"key": "first", "val": 1}
            assert second.model_dump() == {"key": "second", "val": 2}

    async def query(self) -> None:
        pass
