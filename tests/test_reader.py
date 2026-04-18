from unittest.mock import AsyncMock, MagicMock

from pydantic import BaseModel
from pytest import fixture, raises

from pyclickhouse import Admin, Client, Query, Registry, Table
from pyclickhouse.reader import Reader, ReaderError


class Data(BaseModel):
    name: str
    value: int


@fixture
def mock_client() -> MagicMock:
    client = MagicMock()
    client.create_query_context = MagicMock()
    query_result = MagicMock()
    client.query = AsyncMock(return_value=query_result)
    client.query_row_block_stream = AsyncMock()
    return client


class TestReader:
    async def test_reader_init(self, mock_client: MagicMock) -> None:
        reader = Reader(select="SELECT 1", client=mock_client)
        assert reader._client is not None
        assert reader.select == "SELECT 1"
        assert reader.read_rows == 0
        assert reader.model is None

    async def test_reader_init_with_model(self, mock_client: MagicMock) -> None:
        reader = Reader(select="SELECT 1", client=mock_client, model=Data)
        assert reader.model == Data

    async def test_reader_without_client(self, mock_client: MagicMock) -> None:
        reader = Reader(select="SELECT 1")
        assert reader._client is None

        with raises(ReaderError):
            await reader.query()

        reader.bind(mock_client)
        assert reader._client is not None

        mock_client.query.return_value.named_results.return_value = [
            {"name": "one", "value": 1}
        ]

        data = await reader.query()
        assert len(data) == 1
        assert data[0] == {"name": "one", "value": 1}
        assert reader.read_rows == 1

    async def test_reader_query(self, mock_client: MagicMock) -> None:
        reader = Reader(select="SELECT 1", client=mock_client)
        mock_client.query.return_value.named_results.return_value = [
            {"name": "one", "value": 1},
            {"name": "two", "value": 2},
        ]

        data = await reader.query()
        assert len(data) == 2
        assert data[0] == {"name": "one", "value": 1}
        assert data[1] == {"name": "two", "value": 2}
        assert reader.read_rows == 2

    async def test_reader_query_with_model(self, mock_client: MagicMock) -> None:
        reader = Reader(select="SELECT 1", client=mock_client, model=Data)
        mock_client.query.return_value.named_results.return_value = [
            {"name": "one", "value": 1},
            {"name": "two", "value": 2},
        ]

        data = await reader.query()
        assert len(data) == 2
        assert isinstance(data[0], Data)
        assert isinstance(data[1], Data)
        assert data[0].name == "one"
        assert data[1].name == "two"
        assert reader.read_rows == 2

    async def test_reader_stream(self, mock_client: MagicMock) -> None:
        reader = Reader(select="SELECT 1", client=mock_client)

        block1 = [["one", "1"]]
        block2 = [["two", "2"]]

        async def async_iter():
            yield block1
            yield block2

        mock_stream = MagicMock()
        mock_stream.__aenter__ = AsyncMock(return_value=async_iter())
        mock_stream.__aexit__ = AsyncMock()
        mock_stream.__aiter__ = lambda self: async_iter()
        mock_stream.source = MagicMock()
        mock_stream.source.column_names = ["name", "value"]
        mock_client.query_row_block_stream.return_value = mock_stream

        result = await reader.stream()
        data = [item async for item in result]
        assert len(data) == 2
        assert data[0] == {"name": "one", "value": "1"}
        assert data[1] == {"name": "two", "value": "2"}
        assert reader.read_rows == 2

    async def test_reader_integration(self, client: Client) -> None:
        registry = Registry()
        admin = Admin(client)

        class Store(BaseModel):
            name: str
            value: int

        table = Table(Store, name="test_reader", registry=registry)
        await admin.create_all(registry)

        # from table
        data = [(f"name_{i}", i) for i in range(1, 101)]

        await client.insert(
            table=table.get_name(),
            data=data,
        )

        reader = Reader(table, client=client)
        assert reader.read_rows == 0
        await reader.query()
        assert reader.read_rows == 100

        # from query
        query = Query("system.numbers").select("number").take(3)

        # non-stream
        reader = Reader(query, client=client)
        assert reader.read_rows == 0
        data = await reader.query()
        assert data == [{"number": 0}, {"number": 1}, {"number": 2}]
        assert reader.read_rows == 3

        # stream
        reader = Reader(query, client=client)
        assert reader.read_rows == 0
        result = await reader.stream()
        data = []
        async for item in result:
            data.append(item)
        assert data == [{"number": 0}, {"number": 1}, {"number": 2}]
        assert reader.read_rows == 3

        # with model
        class Number(BaseModel):
            number: int

        query = Query("system.numbers").select("number").take(2)
        reader = Reader(query, client=client, model=Number)
        assert reader.read_rows == 0
        result = await reader.stream()
        data = []
        async for item in result:
            data.append(item)
        assert data == [Number(number=0), Number(number=1)]
        assert reader.read_rows == 2

        # with parameters
        class Params(BaseModel):
            max: int

        query = "SELECT number FROM system.numbers WHERE number < {max:Int8}"
        reader = Reader(query, client=client, model=Number, parameters=Params)
        assert reader.read_rows == 0
        result = await reader.stream(Params(max=3))
        data = []
        async for item in result:
            data.append(item)
        assert data == [Number(number=0), Number(number=1), Number(number=2)]
        assert reader.read_rows == 3

        # cleanup
        await admin.drop_all(registry)
