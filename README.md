# pyclickhouse

A modern async Python ORM for ClickHouse

## Features
* Async first design: non-blocking API built around async/await
* Pluggable drivers: choose between `clickhouse-connect` or `asynch`
* Typed models: Define schemas with `pydantic` models for validation and serialization
* Database management: create and manage tables/views
* Query builder: build expressive and composable queries using `prql`
* Batch writer: Validate and insert data in batches

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

from pyclickhouse import get_client, engines, Column, Table, Query, F

async def main() -> None:
    client = get_client("clickhouse://localhost:9000/default")
    
    # model for table management and serialization
    class Event(BaseModel):
        name: Annotated[str, Column(type="String")]
        value: Annotated[int, Column(type="Int32")]

    # define tables
    table = Table(Event, engine=engines.MergeTree(order_by="name"))
    
    async with client:
        # create table
        await client.admin().create_all()
        
        # insert 
        async with client.writer(table) as writer:
            await writer.insert(Event(name="first", value=1))
            await writer.insert(Event(name="second", value=2))
            
        # query
        query = Query(table).filter(table.name == "test_event")
        results = await client.reader(query, response_model=Event).query()
        
        for row in results:
            print(row)
        # Event(name="first", value=1)
        # Event(name="second", value=2)
        
        # aggregate
        query = Query(table).aggregate(res=F.sum(table.value))
        results = await client.reader(query).query()
        print(results)
        # [{"res": 3}]

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## Roadmap

* Support complex datatypes: Nested, Array, Tuple, JSON
* Support table joins and windows
* Support for file based migrations

## License
[MIT License](LICENSE)
