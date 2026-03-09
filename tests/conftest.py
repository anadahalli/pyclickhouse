from typing import AsyncIterator, Iterator

import pytest

from pyclickhouse.client import HttpClient, NativeClient

from .container import ClickHouseContainer


@pytest.fixture(scope="session")
def clickhouse() -> Iterator[ClickHouseContainer]:
    with ClickHouseContainer() as container:
        yield container


@pytest.fixture
async def native_client(clickhouse: ClickHouseContainer) -> AsyncIterator[NativeClient]:
    async with NativeClient(clickhouse.get_native_url()) as client:
        yield client


@pytest.fixture
async def http_client(clickhouse: ClickHouseContainer) -> AsyncIterator[HttpClient]:
    async with HttpClient(clickhouse.get_http_url()) as client:
        yield client
