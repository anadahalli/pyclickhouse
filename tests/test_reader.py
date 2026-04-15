# from clickhouse_connect.driver.exceptions import DatabaseError
from pydantic import BaseModel

from pyclickhouse import (
    Admin,
    Client,
    Query,
    Reader,
    Registry,
    Table,
)


class TestReader:
    async def test_reader_integration(self, client: Client) -> None:
        registry = Registry()
        admin = Admin(client)

        class Store(BaseModel):
            name: str
            value: int

        table = Table(Store, name="test_reader", registry=registry)
        await admin.create_all(registry)

        data = [(f"name_{i}", i) for i in range(1, 101)]

        await client.insert(
            table=table.get_name(),
            data=data,
        )

        query = Query(table).sort(table.value)
        reader = Reader(client, query, stream=True)
        assert reader.read_rows == 0
        result = reader.query()
        async for item in result:
            pass
        assert reader.read_rows == 100

    async def test_reader(self, client: Client) -> None:
        query = Query("system.numbers").select("number").take(3)
        # non-stream
        reader = Reader(client, query, stream=False)
        assert reader.read_rows == 0
        result = reader.query()
        data = []
        async for item in result:
            data.append(item)
        assert data == [{"number": 0}, {"number": 1}, {"number": 2}]
        assert reader.read_rows == 3
        # stream
        reader = Reader(client, query, stream=True)
        assert reader.read_rows == 0
        result = reader.query()
        data = []
        async for item in result:
            data.append(item)
        assert data == [{"number": 0}, {"number": 1}, {"number": 2}]
        assert reader.read_rows == 3

        # with model
        class Number(BaseModel):
            number: int

        query = Query("system.numbers").select("number").take(2)
        reader = Reader(client, query, stream=True, model=Number)
        assert reader.read_rows == 0
        result = reader.query()
        data = []
        async for item in result:
            data.append(item)
        assert data == [Number(number=0), Number(number=1)]
        assert reader.read_rows == 2

        # with parameters
        class Params(BaseModel):
            max: int

        query = "SELECT number FROM system.numbers WHERE number < {max:Int8}"
        reader = Reader(client, query, stream=True, model=Number, parameters=Params)
        assert reader.read_rows == 0
        result = reader.query(Params(max=3))
        data = []
        async for item in result:
            data.append(item)
        assert data == [Number(number=0), Number(number=1), Number(number=2)]
        assert reader.read_rows == 3
