from typing import Any, AsyncIterator, Iterator

from pytest import fixture
from testcontainers.core.container import DockerContainer
from testcontainers.core.wait_strategies import HttpWaitStrategy

from pyclickhouse.client import Client

CLICKHOUSE_IMAGE = "clickhouse/clickhouse-server:latest"


class ClickHouseContainer(DockerContainer):
    def __init__(self, image: str = CLICKHOUSE_IMAGE, **kwargs: Any) -> None:
        super().__init__(image, **kwargs)
        # self.with_exposed_ports(9000)
        self.with_exposed_ports(8123)
        self.with_env("CLICKHOUSE_USER", "default")
        self.with_env("CLICKHOUSE_PASSWORD", "default")
        self.with_env("CLICKHOUSE_DB", "default")
        self._wait_strategy = HttpWaitStrategy(8123).for_status_code(200)

    def get_config(self) -> dict[str, Any]:
        host = self.get_container_host_ip()
        port = self.get_exposed_port(8123)
        return {
            "host": host,
            "port": port,
            "username": "default",
            "password": "default",
            "database": "default",
        }


@fixture(scope="session")
def clickhouse() -> Iterator[ClickHouseContainer]:
    with ClickHouseContainer() as container:
        yield container


@fixture
async def client(clickhouse: ClickHouseContainer) -> AsyncIterator[Client]:
    async with Client(**clickhouse.get_config()) as client:
        yield client
