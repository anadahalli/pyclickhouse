from typing import Any

from clickhouse_connect.driver import _parse_connection_params
from clickhouse_connect.driver.aiohttp_client import AiohttpAsyncClient

from pyclickhouse.settings import Settings


class Client(AiohttpAsyncClient):
    def __init__(self, **kwargs: Any) -> None:
        client_settings = Settings(**kwargs)
        client_kwargs = client_settings.client_kwargs()

        host, username, password, port, database, interface = _parse_connection_params(
            host=client_settings.host,
            port=client_settings.port,
            username=client_settings.username,
            password=client_settings.password,
            database=client_settings.database,
            interface=client_settings.interface,
            secure=client_settings.secure,
            dsn=client_settings.dsn,
            kwargs=client_kwargs,
        )

        super().__init__(
            dsn=None,
            interface=interface,
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
            **client_kwargs,
        )


def create_async_client(**kwargs: Any) -> Client:
    """
    Create a new ClickHouse client.

    Refer to `clickhouse_connect.create_async_client` for more details.
    """
    return Client(**kwargs)
