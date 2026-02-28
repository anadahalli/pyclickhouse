from typing import Iterator

import pytest

from .container import ClickHouseContainer


@pytest.fixture(scope="session")
def clickhouse() -> Iterator[ClickHouseContainer]:
    with ClickHouseContainer() as container:
        yield container
