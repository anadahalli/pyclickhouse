from unittest.mock import AsyncMock, MagicMock

from clickhouse_connect.driver.summary import QuerySummary
from pydantic import BaseModel
from pytest import fixture, raises

from pyclickhouse import (
    Admin,
    Client,
    Registry,
    Table,
    Writer,
)


@fixture
def mock_client() -> MagicMock:
    client = MagicMock()
    client.create_insert_context = AsyncMock()
    insert = AsyncMock()
    insert.return_value = QuerySummary({"written_rows": 1})
    client.data_insert = insert
    return client


class Data(BaseModel):
    name: str
    value: int


registry = Registry()
table = Table(Data, name="writer", registry=registry)


class TestWriter:
    async def test_writer_init(self, mock_client: MagicMock) -> None:
        writer = Writer(client=mock_client, table=table)
        # mock_client.create_insert_context.assert_called_once_with(
        #     table="writer",
        #     database=None,
        #     column_names=["name", "value"],
        #     column_type_names=["String", "Int64"],
        #     column_oriented=False,
        #     settings=None,
        #     transport_settings=None,
        # )
        assert writer.table == table
        assert writer.batch is True
        assert writer.batch_size == 1000
        assert writer.model == Data
        assert writer.columns == ["name", "value"]
        assert writer.queue_size == 0
        assert writer.written_rows == 0

        assert writer._serialize(Data(name="one", value=1)) == ["one", 1]
        assert writer._get_next_batch() == []

    async def test_writer_insert_type(self, mock_client: MagicMock) -> None:
        writer = Writer(client=mock_client, table=table, batch=False)

        record = {"name": "one", "value": 1}
        with raises(TypeError):
            await writer.insert(record)  # type: ignore

    async def test_writer_insert_non_batch(self, mock_client: MagicMock) -> None:
        writer = Writer(client=mock_client, table=table, batch=False)
        record = Data(name="one", value=1)
        await writer.insert(record)
        context = mock_client.create_insert_context.return_value
        assert context.data == [["one", 1]]
        mock_client.data_insert.assert_called_once_with(context=context)
        assert writer.queue_size == 0
        assert writer.written_rows == 1

    async def test_writer_insert_batch(self, mock_client: MagicMock) -> None:
        writer = Writer(client=mock_client, table=table, batch=True)
        assert writer.queue_size == 0
        assert writer.written_rows == 0
        for i in range(100):
            await writer.insert(Data(name=str(i), value=i))
        assert writer.queue_size == 100
        assert writer.written_rows == 0
        mock_client.data_insert.return_value = QuerySummary({"written_rows": 100})
        await writer.flush()
        assert writer.queue_size == 0
        assert writer.written_rows == 100

    async def test_writer_insert_context(self, mock_client: MagicMock) -> None:
        writer = Writer(client=mock_client, table=table, batch=True)
        mock_client.data_insert.return_value = QuerySummary({"written_rows": 100})
        async with writer:
            for i in range(100):
                await writer.insert(Data(name=str(i), value=i))
                assert writer.queue_size == i + 1
                assert writer.written_rows == 0
        assert writer.queue_size == 0
        assert writer.written_rows == 100

    async def test_writer_integration(self, client: Client) -> None:
        # create tables
        admin = Admin(client)
        await admin.create_all(registry)

        batch_size = 100
        writer = Writer(client, table, batch_size=batch_size)

        async with writer:
            for i in range(batch_size - 1):
                await writer.insert(Data(name=str(i), value=i))
            assert writer.queue_size == batch_size - 1
            assert writer.written_rows == 0
        assert writer.written_rows == batch_size - 1

        query = f"SELECT count(*) FROM {table.get_name()}"
        result = await client.command(query)
        assert result == batch_size - 1

        await admin.drop_all(registry)
