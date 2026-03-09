# Introduction

Python async [ClickHouse](https://clickhouse.com/) ORM using [Pydantic](https://docs.pydantic.dev/)

## Features
* Async database operations using `asynch`
* Typed tables using `pydantic`
* Query builder using `prql`

## Installation

using `uv`
```sh
uv add pyclickhouse
```
or with `pip`
```sh
pip install pyclickhouse
```

## Quickstart

```py
from pyclickhouse import ClickHouse, Query, table
from pydantic import BaseModel

# define model
class Store(BaseModel):
    name: str
    value: int

# define table
store = table(Store)

# create connection
db = ClickHouse("clickhouse://localhost:9000")

async with db:
    # create table
    await db.create_table(store)
    
    # insert some data
    await db.insert(Store(name="test", value=1))
    
    # build a query
    query = Query(store).filter(store.name == "test")
    
    # execute the query
    result = await db.query(query, model=Store)
    
    # fetch first result
    print(await result.fetchone())
    # Store(name="test", value=1)

```

---

## Admin
* create_database
* drop_database
* create_table
* drop_table
* list_tables
* get_table
* alter_table

## Reader
* query - stream

## Writer
* insert - batch

## Migrate

## Registry

---

## Table
* Column
* Expression
* Function
* TableConfig

### Table
* to_create_sql
* to_drop_sql
* to_insert_sql

## TableConfig
* name
* engine
* registry

* indexes
* projections
* constraints

---

---

## DataTypes

### String
* String
* FixedString

### Numeric
* Int8
* ...
* BigInt
* Float
* ...
* Boolean
* Enum
* ...
* Decimal
* ...
* BigDecimal
* Interval
* ...

### Temporal
* Date
* Date32
* DateTime
* DateTime64
* Time
* Time64

### Container
* Array
* Tuple
* Map
* Nested

### Network
* IPv4
* IPv6

### Special
* UUID
* JSON
* LowCardinality
* Nullable

### Engines

* Memory

* MergeTree
* ReplacingMergeTree
* CoalescingMergeTree
* SummingMergeTree
* AggregatingMergeTree
* CollapsingMergeTree
* VersionedCollapsingMergeTree

* Kafka
* PostgreSQL
