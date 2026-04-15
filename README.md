# pyclickhouse

A modern async Python ORM for ClickHouse

## Features
* Async first design: non-blocking API built around async/await using `clickhouse_connect`
* Pydantic models: for table design, serialization and deserialization with auto data types
* Database admin: create and manage tables/views and migrations
* Query builder: build expressive and composable queries using `prql`
* Batch writer: Validate and insert data in batches to tables
* Stream reader: Parameterize queries and deserialize results with support for streaming

## Documentation

Documentation is available at [docs/index.md](docs/index.md)

## Installation

using `uv`

```sh
uv add pyclickhouse
```

using `pip`

```sh
pip install pyclickhouse
```

## Quickstart

```py
from typing import Annotated

from pydantic import BaseModel

import pyclickhouse as ch


async def main() -> None:
    client = ch.create_async_client(dsn="clickhouse://localhost:9000/default")

    # model for table management and serialization
    class Event(BaseModel):
        name: Annotated[str, ch.Column(type="String")]
        value: Annotated[int, ch.Column(type="Int32")]

    # define tables
    table = ch.Table(Event, engine=ch.engines.MergeTree(order_by="name"))

    async with client:
        # create table
        admin = ch.Admin(client)
        await admin.create_table(table)

        # insert
        writer = ch.Writer(client, table)
        async with writer:
            await writer.insert(Event(name="first", value=1))
            await writer.insert(Event(name="second", value=2))

        # build query
        query = ch.Query(table).filter(table.name == "test_event")

        # read
        reader = ch.Reader(client, query, model=Event)
        results = reader.query()

        async for row in results:
            print(row)
        # Event(name="first", value=1)
        # Event(name="second", value=2)

        # aggregate
        query = ch.Query(table).aggregate(res=F.sum(table.value))
        reader = ch.Reader(client, query)
        results = reader.query()
        print(results)
        # [{"res": 3}]


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## License
[MIT License](LICENSE)
