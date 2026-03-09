from typing import Any

from testcontainers.core.container import DockerContainer
from testcontainers.core.wait_strategies import HttpWaitStrategy


class ClickHouseContainer(DockerContainer):
    def __init__(
        self,
        image: str = "clickhouse:latest",
        **kwargs: Any,
    ) -> None:
        super().__init__(image, **kwargs)
        self.with_exposed_ports(8123)
        self.with_exposed_ports(9000)
        self.with_env("CLICKHOUSE_USER", "default")
        self.with_env("CLICKHOUSE_PASSWORD", "default")
        self.with_env("CLICKHOUSE_DB", "default")
        # self._wait_strategy = ContainerStatusWaitStrategy()
        self._wait_strategy = HttpWaitStrategy(8123).for_status_code(200)

    def _configure(self) -> None:
        pass

    def get_url(self) -> str:
        host = self.get_container_host_ip()
        port = self.get_exposed_port(9000)
        return f"clickhouse://default:default@{host}:{port}/default"

    def get_native_url(self) -> str:
        host = self.get_container_host_ip()
        port = self.get_exposed_port(9000)
        return f"clickhouse://default:default@{host}:{port}/default"

    def get_http_url(self) -> str:
        host = self.get_container_host_ip()
        port = self.get_exposed_port(8123)
        return f"clickhouse://default:default@{host}:{port}/default"
