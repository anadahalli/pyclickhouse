from typing import cast

import pytest
from clickhouse_connect.driver.exceptions import DatabaseError
from pydantic import BaseModel

from pyclickhouse.client import HttpClient
from pyclickhouse.fields import Aggregate, F, Param
from pyclickhouse.query import Query
from pyclickhouse.reader import Reader
from pyclickhouse.table import Table


class TestReader:
    async def test_reader(self, http_client: HttpClient) -> None:
        client = http_client
        admin = client.admin()

        class Store(BaseModel):
            name: str
            value: int

        table = Table(Store, name="test_reader")
        await admin.create_all()

        writer = client.writer(table)

        items = []
        async with writer:
            for i in range(100):
                item = Store(name=f"name_{i}", value=i)
                items.append(item)
                await writer.insert(item)

        query = Query(table).sort(table.value)
        reader = Reader(client, query, response_model=Store)
        assert reader.read_rows == 0

        await reader.query() == items
        assert reader.read_rows == 100

        reader = client.reader(query)
        assert isinstance(reader, Reader)
        assert reader._client is client

        await admin.truncate_table(table)

        async with writer:
            for i in range(1, 1001):
                name = i % 10
                await writer.insert(Store(name=str(name), value=1))

        # without response model
        query = (
            Query(table)
            .group(
                key=table.name,
                val=Aggregate(F.sum(table.value)),
            )
            .sort("key")
        )

        reader = Reader(client, query)

        result = await reader.query()
        assert len(result) == 10
        assert result[0] == {"key": "0", "val": 100}

        # with args
        query = Query(table).group(table.name).filter(table.name == Param("name"))

        reader = Reader(client, query)

        with pytest.raises(DatabaseError):
            await reader.query()

        result = await reader.query({"name": "0"})
        assert result[0] == {"name": "0"}

        class Args(BaseModel):
            name: str

        result = await reader.query(Args(name="1"))
        assert result[0] == {"name": "1"}

        # with skip and limit
        query = Query("numbers", database="system").take(100)
        reader = Reader(client, query)

        result = await reader.query()
        result = cast(list[dict], result)
        assert len(result) == 100
        assert result[0]["number"] == 0
        assert result[-1]["number"] == 99

        result = await reader.query(skip=10)
        result = cast(list[dict], result)
        assert len(result) == 90
        assert result[0]["number"] == 10
        assert result[-1]["number"] == 99

        result = await reader.query(limit=20)
        result = cast(list[dict], result)
        assert len(result) == 20
        assert result[0]["number"] == 0
        assert result[-1]["number"] == 19

        result = await reader.query(skip=10, limit=30)
        result = cast(list[dict], result)
        assert len(result) == 30
        assert result[0]["number"] == 10
        assert result[-1]["number"] == 39
