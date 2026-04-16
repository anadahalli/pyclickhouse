---
title: Query Builder
---

Query builder using [PRQL](https://prql-lang.org/) to create expressive and flexible analytics queries.

Data transformations/pipelines can be chained togethor with these method:

* select
* derive
* filter
* aggregate
* group
* sort
* take

Uses `prqlc` to compile to SQL string with support for parameterized queries.

The order of operations matter as every operation will add a new pipeline to the query.

---

## Basic Usage

```py
from pyclickhouse import Query, Aggregate, Param, Table, F
from pydantic import BaseModel

# define our table model
class Store(BaseModel):
    name: str
    value: int

# create a table definition
store = Table(model=Store, name="store")

# query from table
query = Query(store)

# chain other operations to query
query = query.select(table.name)

# compile to SQL
print(query.compile())
# "SELECT name FROM store"

# build pipeline
print(query.build())
# from store | select {name}
```

---

## Parameters

> SQL: `{<param_name>:<param_clickhouse_type>}}`

> PRQL: `s'{<param_name>:<param_clickhouse_type>}`

Add a parameter to a filterd value
```py
query.filter(store.value >= Param(value, int))
```

Provide parameter value during query
```
client.query(str(query), parameters={"value": 10})
```

---

## Pipelines 

### Select
Pick or compute columns

> SQL: `SELECT ...`

> PRQL: `select {name = expression, column}`

With default column names
```py
query.select(table.name, table.value)

# SQL: SELECT name, value
# PRQL select {name, value}
```

With custom columns names
```py
query.select(my_name=table.name, my_value=table.value)

# SQL: SELECT name AS my_name, value AS my_value
# PRQL: select {my_name = name, my_value = value}
```

### Derive
Compute new columns

> SQL: `SELECT ...`

> PRQL: `derive {name = expression}`

```py
query.derive(new_value=table.value + 1)
```

### Filter
Pick rows based on their values.

> SQL: `WHERE ...`

> PRQL: `filter boolean_expression`

```py
query.filter(store.value >= 10)
```


### Aggregate
Summarize many rows into one row

Without `group`, it produces one row from the whole table

> SQL: `function(expression) ...`

> PRQL: `aggregate {expression or assign operations}`

```py
query.aggregate(value_sum=F.sum(store.value))

# SQL: count(value) AS value_sum
```

### Group
Group by columns.

Within a group, `aggregate` produces one row for each group

> SQL: `GROUP BY ...`

> PRQL: `group {key_columns} (pipeline)`

Group by columns without aggregations
```py
query.group(store.name)

# SQL: GROUP BY name
```

Group by columns with aggregations
```py
query.group(store.name, Aggregate(F.count(store.value)))

# SQL: SELECT name, count(value) ... GROUP BY name
```

### Sort
Order rows based on the values of one or more expressions

> SQL: `ORDER BY`
> PRQL: `sort {(+|-) column}`

Ascending order (default)
```py
query.sort(store.value)
```

Descending order
```py
query.sort(-store.value)
```

### Take
Picks rows based on their position
> SQL `LIMIT or OFFSET`

> PRQL `take (n|range)`

Limit selection to `n` rows
```py
query.take(10)
# SQL: LIMIT 10
```

With both start and end
```py
query.take(start=10, end=21)
# SQL: LIMIT 10 OFFSET 9
```

Start selection from
```py
query.take(start=10)
# SQL: OFFSET 9
```

End selection to
```py
query.take(end=21)
# SQL: LIMIT 10 OFFSET 9
```

--- 

Learn more about PRQL [here](https://prql-lang.org/book/index.html)
