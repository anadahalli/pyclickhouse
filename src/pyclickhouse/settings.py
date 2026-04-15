from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="allow", env_prefix="CLICKHOUSE_")

    dsn: str | None = None
    interface: str = "http"
    host: str = "localhost"
    port: int = 8123
    username: str | None = None
    password: str = ""
    database: str = "__default__"
    access_token: str | None = None
    secure: bool = False
    compress: bool | str = True
    connect_timeout: int = 10
    send_receive_timeout: int = 300
    client_name: str | None = None
    verify: bool | str = True
    ca_cert: str | None = None
    client_cert: str | None = None
    client_cert_key: str | None = None
    http_proxy: str | None = None
    https_proxy: str | None = None
    server_host_name: str | None = None
    tls_mode: str | None = None
    proxy_path: str = ""
    connector_limit: int = 100
    connector_limit_per_host: int = 20
    keepalive_timeout: float = 30.0
    session_id: str | None = None
    settings: dict[str, Any] | None = None
    query_limit: int = 0
    query_retries: int = 2
    apply_server_timezone: str | bool | None = None
    utc_tz_aware: bool | None = None
    show_clickhouse_errors: bool | None = None
    autogenerate_session_id: bool | None = None
    autogenerate_query_id: bool | None = None
    form_encode_query_params: bool = False
