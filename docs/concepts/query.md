---
title: Query 
---

The Query builder provides a fluent, composable API for building ClickHouse queries. It uses [PRQL](https://prql-lang.org/) as an intermediate representation, which compiles to SQL.

Queries are built by chaining pipeline operations together. Each operation returns a new Query, allowing for a functional, immutable approach to query construction.

---

## Overview

The Query builder supports the following operations:

- **select** — Pick or rename columns
- **derive** — Compute new columns from existing ones
- **filter** — Filter rows based on conditions
- **aggregate** — Summarize rows into aggregates
- **group** — Group rows and aggregate by groups
- **sort** — Order rows by expressions
- **take** — Limit and offset rows

---

## Creating a Query

A Query starts from either a `Table` object or a table name string:

```py
from pyclickhouse import Query, Table
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

users = Table(model=User, name="users")

# Create a query from a Table object
query = Query(users)
print(query)
# SELECT * FROM users

# Or create from a table name string
query = Query("users")
print(query)
# SELECT * FROM users
```

### Building vs Compiling

The Query builder distinguishes between two representations:

- **build()** — Show the PRQL pipeline representation
- **compile()** or **str()** — Convert to SQL

```py
query = Query(users).filter(users.id > 10).select(users.name)

print(query.build())
# from users | filter (users.id > 10) | select {name}

print(query.compile())
# SELECT name FROM users WHERE id > 10

print(str(query))  # Same as compile()
# SELECT name FROM users WHERE id > 10
```

---

## Pipeline Operations

### Select

Pick specific columns or rename them.

```py
# Select single column
query = Query(users).select(users.id)
# SELECT id FROM users

# Select multiple columns
query = Query(users).select(users.id, users.name)
# SELECT id, name FROM users

# Select with custom column names
query = Query(users).select(
    user_id=users.id,
    full_name=users.name
)
# SELECT id AS user_id, name AS full_name FROM users

# Mix default and custom names
query = Query(users).select(
    users.email,
    user_id=users.id
)
# SELECT email, id AS user_id FROM users
```

### Derive

Compute new columns based on existing ones. Adds columns to the existing selection.

```py
from pyclickhouse import F

# Add computed columns
query = Query(users).derive(
    name_length=F.length(users.name)
)
# SELECT *, length(name) AS name_length FROM users

# Arithmetic operations
query = Query(products).derive(
    total_price=products.price * products.quantity
)
# SELECT *, price * quantity AS total_price FROM products

# Using functions
query = Query(events).derive(
    hour=F.toStartOfHour(events.timestamp),
    year=F.year(events.timestamp)
)
# SELECT *, toStartOfHour(timestamp) AS hour, year(timestamp) AS year FROM events
```

### Filter

Select rows based on boolean expressions.

```py
# Simple comparison
query = Query(users).filter(users.id > 10)
# SELECT * FROM users WHERE id > 10

# Multiple conditions with AND
query = Query(users).filter(
    (users.id > 10) & (users.name == "Alice")
)
# SELECT * FROM users WHERE id > 10 AND name = 'Alice'

# OR conditions
query = Query(users).filter(
    (users.id == 1) | (users.id == 2)
)
# SELECT * FROM users WHERE id = 1 OR id = 2

# NOT conditions
query = Query(users).filter(~(users.id == 0))
# SELECT * FROM users WHERE NOT id = 0

# IN operator
query = Query(users).filter(users.id.is_in([1, 2, 3]))
# SELECT * FROM users WHERE id IN (1, 2, 3)

# NOT IN operator
query = Query(users).filter(users.name.is_not_in(["admin", "bot"]))
# SELECT * FROM users WHERE NOT name IN ('admin', 'bot')
```

### Sort

Order rows by one or more columns.

```py
# Sort ascending (default)
query = Query(users).sort(users.name)
# SELECT * FROM users ORDER BY name

# Sort descending (using unary minus)
query = Query(users).sort(-users.id)
# SELECT * FROM users ORDER BY id DESC

# Sort by multiple columns
query = Query(events).sort(
    events.date,
    -events.value
)
# SELECT * FROM events ORDER BY date, value DESC
```

### Take

Limit and offset rows for pagination.

```py
# Take first n rows
query = Query(users).take(10)
# SELECT * FROM users LIMIT 10

# Take with offset (start at row 10, take until row 20)
query = Query(users).take(start=10, end=20)
# SELECT * FROM users LIMIT 11 OFFSET 9

# Take from row n onwards
query = Query(users).take(start=100)
# SELECT * FROM users OFFSET 99

# Take up to row n
query = Query(users).take(end=50)
# SELECT * FROM users LIMIT 50
```

### Aggregate

Summarize multiple rows into a single aggregate value. **Note: Do NOT use `Aggregate()` wrapper in `aggregate()` method.**

```py
from pyclickhouse import F

# Count all rows
query = Query(users).aggregate(F.count())
# SELECT count() FROM users

# Named aggregate
query = Query(users).aggregate(
    total_users=F.sum(users.id)
)
# SELECT sum(id) AS total_users FROM users

# Multiple aggregates (NO Aggregate wrapper needed)
query = Query(orders).aggregate(
    order_count=F.count(),
    total_amount=F.sum(orders.amount),
    avg_amount=F.avg(orders.amount)
)
# SELECT count(), sum(amount) AS total_amount, avg(amount) AS avg_amount FROM orders

# Aggregate with count on specific column
query = Query(users).aggregate(
    unique_users=F.uniq(users.id)
)
# SELECT uniq(id) AS unique_users FROM users
```

### Group

Group rows by one or more columns and optionally aggregate. **Use `Aggregate()` wrapper here to distinguish aggregation expressions from grouping columns.**

```py
from pyclickhouse import Aggregate, F

# Group without aggregation
query = Query(users).group(users.name)
# SELECT name FROM users GROUP BY name

# Group with custom name
query = Query(users).group(user_name=users.name)
# SELECT name AS user_name FROM users GROUP BY name

# Group with aggregation (REQUIRES Aggregate wrapper)
query = Query(orders).group(
    orders.customer_id,
    Aggregate(F.count())
)
# SELECT customer_id, count() FROM orders GROUP BY customer_id

# Group with named aggregates (REQUIRES Aggregate wrapper)
query = Query(orders).group(
    orders.customer_id,
    total_orders=Aggregate(F.count()),
    total_amount=Aggregate(F.sum(orders.amount))
)
# SELECT customer_id, count() AS total_orders, sum(amount) AS total_amount FROM orders GROUP BY customer_id

# Group by multiple columns with aggregates
query = Query(sales).group(
    sales.date,
    sales.region,
    count=Aggregate(F.count()),
    total=Aggregate(F.sum(sales.amount))
)
# SELECT date, region, count(), sum(amount) AS total FROM sales GROUP BY date, region
```

---

## Parameterized Queries

Use `Param` to create queries with runtime-bound parameters.

### Using Param

```py
from pyclickhouse import Param

# String parameter (default type)
param = Param("name")
# {name:String}

# Integer parameter
param = Param("user_id", int)
# {user_id:Int64}

# Float parameter
param = Param("min_price", float)
# {min_price:Float64}
```

### Param in Filters

```py
# Filter with parameter
query = Query(users).filter(users.id >= Param("min_id", int))
# SELECT * FROM users WHERE id >= {min_id:Int64}

# Multiple parameters
query = Query(users).filter(
    (users.id >= Param("min_id", int)) &
    (users.name == Param("search_name", str))
)
# SELECT * FROM users WHERE id >= {min_id:Int64} AND name = {search_name:String}
```

### Executing Parameterized Queries

```py
from pyclickhouse import Client, Reader

async def query_with_params():
    client = Client()
    
    query = Query(users).filter(
        users.id >= Param("min_id", int)
    )
    
    async with client:
        reader = Reader(client, query)
        results = await reader.query(
            parameters={"min_id": 100}
        )
        return results
```

---

## Functions with F

The `F` object provides access to ClickHouse functions.

### String Functions

```py
from pyclickhouse import F

# String length
query = Query(users).derive(
    name_length=F.length(users.name)
)

# Case conversion
query = Query(users).derive(
    name_upper=F.upper(users.name),
    name_lower=F.lower(users.name)
)

# Substring
query = Query(users).derive(
    first_char=F.substring(users.name, 1, 1)
)

# Concatenation
query = Query(users).derive(
    full_info=F.concat(users.name, " - ", users.email)
)

# Trim
query = Query(users).derive(
    trimmed_name=F.trim(users.name)
)
```

### Date/Time Functions

```py
# Current date/time
query = Query(events).derive(
    current_time=F.now(),
    current_date=F.today()
)

# Extract date components
query = Query(events).derive(
    year=F.year(events.timestamp),
    month=F.month(events.timestamp),
    day=F.dayOfMonth(events.timestamp),
    hour=F.hour(events.timestamp)
)

# Start of intervals
query = Query(events).derive(
    start_of_day=F.toStartOfDay(events.timestamp),
    start_of_month=F.toStartOfMonth(events.timestamp),
    start_of_hour=F.toStartOfHour(events.timestamp)
)
```

### Math Functions

```py
# Rounding and absolute value
query = Query(metrics).derive(
    rounded=F.round(metrics.value, 2),
    absolute=F.abs(metrics.value),
    square_root=F.sqrt(metrics.value)
)

# Floor and ceiling
query = Query(data).derive(
    floored=F.floor(data.value),
    ceiling=F.ceil(data.value)
)
```

### Aggregate Functions

```py
# Count
F.count()
F.count(users.id)  # Count non-null values

# Sum and average
F.sum(orders.amount)
F.avg(orders.amount)

# Min and max
F.min(metrics.value)
F.max(metrics.value)

# Unique count
F.uniq(users.id)

# Array aggregation
F.groupArray(items.name)

# State functions (for materialized views)
F.sumState(values.amount)
F.avgState(values.amount)
F.countState()

# Merge functions
F.sumMerge(agg_values.amount_state)
F.avgMerge(agg_values.avg_state)
```

---

## Complete Examples

### Example 1: Simple Filtering and Selection

```py
from pyclickhouse import Query, Table
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

users = Table(model=User, name="users")

query = Query(users).filter(users.id > 10).select(users.name)
print(str(query))
# SELECT name FROM users WHERE id > 10
```

### Example 2: Grouping and Aggregation

```py
from pyclickhouse import Query, Table, F, Aggregate

class Order(BaseModel):
    customer_id: int
    amount: float

orders = Table(model=Order, name="orders")

# Orders per customer with totals
query = Query(orders).group(
    orders.customer_id,
    order_count=Aggregate(F.count()),
    total_spent=Aggregate(F.sum(orders.amount)),
    avg_order=Aggregate(F.avg(orders.amount))
)

print(str(query))
# SELECT customer_id, count() AS order_count, sum(amount) AS total_spent, avg(amount) AS avg_order
# FROM orders GROUP BY customer_id
```

### Example 3: Time Series Aggregation

```py
from pyclickhouse import Query, Table, F, Aggregate

class Metric(BaseModel):
    timestamp: str
    service: str
    cpu_usage: float

metrics = Table(model=Metric, name="metrics")

# Hourly stats by service
query = Query(metrics).group(
    service=metrics.service,
    hour=F.toStartOfHour(metrics.timestamp),
    avg_cpu=Aggregate(F.avg(metrics.cpu_usage)),
    max_cpu=Aggregate(F.max(metrics.cpu_usage))
).sort(metrics.service, -F.toStartOfHour(metrics.timestamp))

print(str(query))
# SELECT service, toStartOfHour(timestamp) AS hour, avg(cpu_usage) AS avg_cpu, max(cpu_usage) AS max_cpu
# FROM metrics GROUP BY service, toStartOfHour(timestamp) ORDER BY service, toStartOfHour(timestamp) DESC
```

### Example 4: Filtering with Aggregation

```py
from pyclickhouse import Query, Table, F

class Event(BaseModel):
    user_id: int
    event_type: str
    value: float

events = Table(model=Event, name="events")

# High-value purchases
query = Query(events).filter(
    (events.event_type == "purchase") & (events.value > 100)
).sort(-events.value).take(10)

print(str(query))
# SELECT * FROM events WHERE event_type = 'purchase' AND value > 100 ORDER BY value DESC LIMIT 10
```

### Example 5: Parameterized Query

```py
from pyclickhouse import Query, Table, Param

users = Table(model=User, name="users")

query = Query(users).filter(
    users.id >= Param("min_id", int)
).filter(
    users.name == Param("search_name", str)
)

print(str(query))
# SELECT * FROM users WHERE id >= {min_id:Int64} AND name = {search_name:String}
```

### Example 6: Derive with Functions

```py
from pyclickhouse import Query, Table, F

class Product(BaseModel):
    name: str
    price: float
    quantity: int

products = Table(model=Product, name="products")

query = Query(products).derive(
    total_value=products.price * products.quantity,
    name_length=F.length(products.name),
    price_rounded=F.round(products.price, 2)
)

print(str(query))
# SELECT *, price * quantity AS total_value, length(name) AS name_length, round(price, 2) AS price_rounded FROM products
```

---

## Aggregate vs Group

Key difference:

- **`aggregate()`** — Summarizes the entire result set into one row. **No `Aggregate()` wrapper needed.**
- **`group()`** — Summarizes results per group. **Use `Aggregate()` wrapper to mark aggregate functions.**

```py
# aggregate() - one row total
query = Query(orders).aggregate(
    total_orders=F.count(),
    total_amount=F.sum(orders.amount)
)
# SELECT count() AS total_orders, sum(amount) AS total_amount FROM orders

# group() - one row per group
query = Query(orders).group(
    orders.customer_id,
    total_orders=Aggregate(F.count()),
    total_amount=Aggregate(F.sum(orders.amount))
)
# SELECT customer_id, count() AS total_orders, sum(amount) AS total_amount FROM orders GROUP BY customer_id
```

---

## Learn More

- [PRQL Documentation](https://prql-lang.org/) — Learn about PRQL language features
- [ClickHouse Functions](https://clickhouse.com/docs/sql-reference/functions) — Complete function reference
- [Reader](/concepts/reader) — Execute queries and retrieve results
- [Table](/concepts/table) — Define tables and access columns
- [View](/concepts/view) — Create and manage views
