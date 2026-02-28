# pyclickhouse

Python async ClickHouse ORM using Pydantic

## Features
* Async database operations using `asynch`
* Typed tables using `pydantic`
* Query builder using `prql`

Check the [documentation](docs/index.md) for more details.

---

## Installation
```sh
uv add git+https://github.com/anadahalli/pyclickhouse.git
```

## Quickstart

Initialize client
```py
from pyclickhouse import Database, Table, Query

db = Database("clickhouse://localhost:9000/default")

# run operations in an async context manager
async with db:
    ...
```

Define table
```py
class Event(Table):
    name: str
    value: int
```

Create table
```py
await db.create_table(Event)
```

Insert table
```py
await db.insert(Event(name="example", value=1))
```
Query table
```py
# filter
q = Query(Event).filter(Event.name == "example")
events = await db.query(q)
for event in events:
    print(event)
# Event(name="example", value=1)

# aggregate
q = Query(Event).aggregate(res=F.sum(Event.value))
total = await db.query(q)
print(total.first())
# Result(res=1)
```
---

## Documentation
* Database
* Table
* Config
* Column
* Engine
* Expression
* Function
* Query

---

## License
[MIT License](LICENSE)
