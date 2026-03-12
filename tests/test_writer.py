from collections import deque

import pytest
from pydantic import BaseModel

from pyclickhouse import (
    HttpClient,
    Registry,
    Table,
    Writer,
)


class TestWriter:
    async def test_writer(self, http_client: HttpClient) -> None:
        client = http_client
        registry = Registry()

        class Data(BaseModel):
            name: str
            value: int

        table = Table(Data, name="writer", registry=registry)

        await client.admin().create_all(registry)

        writer = client.writer(table)
        assert isinstance(writer, Writer)
        assert writer._client is client
        assert writer.written_rows == 0

        with pytest.raises(TypeError):

            class Random(BaseModel):
                name: str

            await writer.insert(Random(name="test"))

        data = Data(name="one", value=1)
        await writer.insert(data)
        assert writer.written_rows == 0
        assert writer._records == deque([data])
        await writer.flush()
        assert writer.written_rows == 1

        batch_size = 100
        writer = Writer(client, table, batch_size=batch_size)

        async with writer:
            for i in range(batch_size):
                await writer.insert(Data(name=str(i), value=i))
            assert writer.queue_length == batch_size
            assert writer.written_rows == 0
        assert writer.written_rows == batch_size

        query = f"SELECT count(*) FROM {table.get_name()}"
        result = await client.query(query)
        assert result.rows[0][0] == batch_size + 1
