---
title: Async Client
---

The `Client` is the main async interface for connecting to and interacting with ClickHouse. 

It wraps the `clickhouse_connect` library and provides methods for executing queries, managing tables/views, and inserting data.

---

## Creating a Client

### Quick Start

Create and initialize a client in one step:

```py
from pyclickhouse import create_async_client

client = await create_async_client()
```

This uses default settings or reads from environment variables.

### Manual Initialization

For more control, create a `Client` instance and use it as an async context manager:

```py
from pyclickhouse import Client

client = Client()

async with client:
    # execute queries
    result = await client.query("SELECT 1")
```

---

## Configuration

### Environment Variables

Configure ClickHouse connection using environment variables with the `CLICKHOUSE_` prefix:

```sh
CLICKHOUSE_HOST=localhost
CLICKHOUSE_PORT=8123
CLICKHOUSE_DATABASE=default
CLICKHOUSE_USERNAME=default
CLICKHOUSE_PASSWORD=password
CLICKHOUSE_SECURE=false
```

Then create a client:

```py
from pyclickhouse import create_async_client

# Automatically reads from environment variables
client = await create_async_client()
```

### Explicit Configuration

Pass settings directly as keyword arguments:

```py
from pyclickhouse import Client

client = Client(
    host="localhost",
    port=8123,
    database="default",
    username="default",
    password="password"
)

async with client:
    result = await client.query("SELECT 1")
```

Or use the `Settings` class:

```py
from pyclickhouse import Client, Settings

settings = Settings(
    host="localhost",
    port=8123,
    database="default",
    username="default",
    password="password"
)

client = Client(**settings.model_dump())

async with client:
    result = await client.query("SELECT 1")
```

See [Settings](/references/settings) for all available configuration options including SSL, proxy, compression, and timeouts.

---

## Basic Usage

### Execute Raw SQL

```py
async with client:
    result = await client.query("SELECT * FROM system.tables LIMIT 5")
    print(result)
```

### Execute with Parameters

```py
async with client:
    result = await client.query(
        "SELECT * FROM my_table WHERE id = {id:Int32}",
        parameters={"id": 42}
    )
```

### Insert Data Directly

```py
async with client:
    await client.insert(
        "INSERT INTO my_table VALUES",
        [(1, "Alice"), (2, "Bob")]
    )
```

### Execute Commands

```py
async with client:
    await client.command("CREATE DATABASE IF NOT EXISTS my_db")
```

### Context Manager (Recommended)

Always use the client as an async context manager to ensure the connection is properly closed:

```py
async with client:
    # connection is active here
    result = await client.query("SELECT 1")
    
# connection is automatically closed
```

---

## Working with Tables

### Create a Table

Define a Pydantic model and create a table from it:

```py
from pydantic import BaseModel
from pyclickhouse import Admin, Table

class User(BaseModel):
    id: int
    name: str
    email: str

users = Table(model=User, name="users")

async with client:
    admin = Admin(client)
    await admin.create_table(users)
```

### Insert Data with Writer

Use the `Writer` class for efficient batch inserts with validation:

```py
from pyclickhouse import Writer

users_data = [
    User(id=1, name="Alice", email="alice@example.com"),
    User(id=2, name="Bob", email="bob@example.com"),
]

async with client:
    writer = Writer(client, users)
    async with writer:
        for user in users_data:
            await writer.insert(user)
```

### Query Data with Reader

Use the `Reader` class to query and validate results:

```py
from pyclickhouse import Reader

async with client:
    reader = Reader(client, users, model=User)
    results = await reader.query()
    
    for user in results:
        print(user)  # User objects with validation
```

### Stream Results

For large result sets, stream data without loading everything into memory:

```py
async with client:
    reader = Reader(client, users, model=User)
    results = await reader.stream()
    
    async for user in results:
        print(user)
```

---

## Query Builder

Compose queries programmatically using the `Query` builder:

```py
from pyclickhouse import Query, F

query = (
    Query(users)
    .filter(users.id > 10)
    .select(users.name, users.email)
    .sort(-users.id)
    .take(100)
)

async with client:
    result = await client.query(query.compile())
```

See [Query Builder](/concepts/query) for more details on composing queries.

---

## Complete Example

Here's a complete example combining all features:

```py
from pydantic import BaseModel
from pyclickhouse import Admin, Client, F, Query, Reader, Table, Writer

class Event(BaseModel):
    name: str
    value: int

async def main():
    client = Client()
    
    # Define a table
    events = Table(model=Event, name="events")
    
    async with client:
        # Create table
        admin = Admin(client)
        await admin.create_table(events)
        
        # Insert data
        writer = Writer(client, events)
        async with writer:
            await writer.insert(Event(name="first", value=1))
            await writer.insert(Event(name="second", value=2))
        
        # Query data
        reader = Reader(client, events, model=Event)
        results = await reader.stream()
        async for event in results:
            print(event)
        
        # Aggregate with query builder
        query = Query(events).aggregate(total=F.sum(events.value))
        reader = Reader(client, query)
        result = await reader.query()
        print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

---

## Error Handling

The client raises exceptions for connection and query errors:

```py
from clickhouse_connect.exc import ClickHouseException

async with client:
    try:
        result = await client.query("SELECT * FROM nonexistent_table")
    except ClickHouseException as e:
        print(f"ClickHouse error: {e}")
```

---

## Advanced Configuration

### SSL/TLS

```py
client = Client(
    host="clickhouse.example.com",
    secure=True,
    verify=True,  # Verify SSL certificate
    ca_cert="/path/to/ca.crt"
)
```

### Proxy

```py
client = Client(
    host="localhost",
    http_proxy="http://proxy.example.com:8080",
    https_proxy="https://proxy.example.com:8443"
)
```

### Connection Pooling

```py
client = Client(
    host="localhost",
    connector_limit=100,  # Max total connections
    connector_limit_per_host=20  # Max connections per host
)
```

### Compression

```py
client = Client(
    host="localhost",
    compress=True  # Enable compression for queries and responses
)
```

### Timeouts

```py
client = Client(
    host="localhost",
    connect_timeout=10,  # Connection timeout in seconds
    send_receive_timeout=300  # Query timeout in seconds
)
```

---

Learn more about the [Client API](/references/client), [Admin](/concepts/admin), [Query Builder](/concepts/query), and other ORM features.
