# pyclickhouse

A modern async Python ORM for ClickHouse using Pydantic.

## Features
* **Async** http client using `clickhouse_connect`
* **Model** data using `pydantic` for table with auto data types
* **Query** builder using `prql` to create composable queries
* **Admin** to create and manage tables/views and migrations
* **Writer** to validate and insert data in batches to tables
* **Reader** to query and stream results with validation

## Documentation
Documentation is available at [docs/](/)

---

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
from pydantic import BaseModel

from pyclickhouse import Admin, Client, F, Query, Reader, Table, Writer


async def main() -> None:
    # create new client
    client = Client()

    # define your model
    class Event(BaseModel):
        name: str
        value: int

    # define a table
    table = Table(Event)

    async with client:
        # create table
        admin = Admin(client)
        await admin.create_table(table)

        # insert event data
        writer = Writer(client, table)
        async with writer:
            await writer.insert(Event(name="first", value=1))
            await writer.insert(Event(name="second", value=2))

        # stream event data
        reader = Reader(client, table, model=Event)
        results = await reader.stream()
        async for row in results:
            print(row)
        # Event(name="first", value=1)
        # Event(name="second", value=2)

        # aggregate using query builder
        query = Query(table).aggregate(res=F.sum(table.value))

        # query event analytics
        reader = Reader(client, query)
        results = await reader.query()
        print(results)
        # [{"res": 3}]


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```
---

## License
[MIT License](LICENSE)
