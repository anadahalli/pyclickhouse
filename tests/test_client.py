from datetime import datetime, timezone

from pyclickhouse.client import Client, HttpClient, NativeClient, QueryResult


async def test_http_client(http_client: HttpClient) -> None:
    assert await http_client.ping()
    await run_simple_test(http_client, table="test_http_simple")
    await run_advanced_test(http_client, table="test_http_advanced")
    await run_datatype_test(http_client, table="test_http_datatype")


async def test_native_client(native_client: NativeClient) -> None:
    assert await native_client.ping()
    await run_simple_test(native_client, table="test_native_simple")
    await run_advanced_test(native_client, table="test_native_advanced")
    await run_datatype_test(native_client, table="test_native_datatype")


async def run_simple_test(client: Client, table: str) -> None:
    # create table
    create_sql = f"CREATE TABLE {table} (name String) ENGINE = Memory"
    assert await client.command(create_sql)

    # insert
    data = [["1"], ["2"], ["3"], ["4"]]
    result = await client.insert(table, data=data)
    assert result == 4

    # query
    query_sql = f"SELECT name FROM {table} ORDER BY name"
    result = await client.query(query_sql)
    assert isinstance(result, QueryResult)
    assert result.columns == {"name": "String"}
    assert result.rows == [("1",), ("2",), ("3",), ("4",)]


async def run_advanced_test(client: Client, table: str) -> None:
    # create table
    create_sql = f"CREATE TABLE {table} (name String, value Int32) ENGINE = Memory"
    assert await client.command(create_sql)

    # insert
    data = [("1", 1), ("2", 2), ("3", 3), ("4", 4)]
    result = await client.insert(table, data=data, columns=["name", "value"])
    assert result == 4

    # query
    query_sql = f"SELECT name, value FROM {table} ORDER BY value"
    result = await client.query(query_sql)
    assert isinstance(result, QueryResult)
    assert result.columns == {"name": "String", "value": "Int32"}
    assert result.rows == [("1", 1), ("2", 2), ("3", 3), ("4", 4)]

    query_sql = f"SELECT value FROM {table} WHERE value > {{val:String}}"
    result = await client.query(query_sql, args={"val": 2})
    assert isinstance(result, QueryResult)
    assert result.columns == {"value": "Int32"}
    assert result.rows == [(3,), (4,)]


async def run_datatype_test(client: Client, table: str) -> None:
    columns = [
        "str_ String",
        "int_ Int32",
        "float_ Float64",
        "bool_ Bool",
        "date_ Date",
        "datetime_ DateTime",
    ]
    create_sql = f"CREATE TABLE {table} ({', '.join(columns)}) ENGINE = Memory"
    assert await client.command(create_sql)

    now_utc = datetime.now(timezone.utc)
    now_naive = now_utc.replace(tzinfo=None, microsecond=0)
    data = (
        "test",
        1,
        2.3,
        True,
        now_utc.date(),
        now_utc,
    )
    result = await client.insert(table, data=[data])
    assert result == 1

    query_sql = f"SELECT * FROM {table}"
    result = await client.query(query_sql)

    assert result.rows[0] == (
        "test",
        1,
        2.3,
        True,
        now_utc.date(),
        now_naive,
    )
