from pyclickhouse.client import Client, HttpClient, NativeClient, QueryResult


async def test_http_client(http_client: HttpClient) -> None:
    await run_client_tests(http_client, table="test_http")


async def test_native_client(native_client: NativeClient) -> None:
    await run_client_tests(native_client, table="test_native")


async def run_client_tests(client: Client, table: str) -> None:
    # connection
    assert await client.ping()

    # command
    create_sql = f"CREATE TABLE {table} (name String) ENGINE = Memory"
    assert await client.command(create_sql)

    # insert
    data = [
        {"name": "1"},
        {"name": "2"},
        {"name": "3"},
        {"name": "4"},
    ]
    result = await client.insert(table, data=data)
    assert result == 4

    # query
    query_sql = f"SELECT name FROM {table} ORDER BY name"
    result = await client.query(query_sql)
    assert isinstance(result, QueryResult)
    assert result.columns == {"name": "String"}
    assert result.rows == [("1",), ("2",), ("3",), ("4",)]
