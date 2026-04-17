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

Summarize the entire result set into aggregate values. Produces a single row with aggregate functions applied to all rows.

**Important:** Do NOT use the `Aggregate()` wrapper in the `aggregate()` method. Use `Aggregate()` only in the `group()` method to distinguish aggregate functions from grouping columns.

#### Basic Aggregation

```py
from pyclickhouse import F

# Count all rows
query = Query(users).aggregate(F.count())
# SELECT count() FROM users

# Count with alias
query = Query(users).aggregate(
    total_users=F.count()
)
# SELECT count() AS total_users FROM users

# Sum specific column
query = Query(users).aggregate(
    total_ids=F.sum(users.id)
)
# SELECT sum(id) AS total_ids FROM users
```

#### Multiple Aggregates

```py
# Multiple aggregates - NO Aggregate wrapper needed
query = Query(orders).aggregate(
    order_count=F.count(),
    total_amount=F.sum(orders.amount),
    avg_amount=F.avg(orders.amount),
    min_amount=F.min(orders.amount),
    max_amount=F.max(orders.amount)
)
# SELECT count() AS order_count, sum(amount) AS total_amount, avg(amount) AS avg_amount, min(amount) AS min_amount, max(amount) AS max_amount FROM orders
```

#### Common Aggregate Functions

```py
# Count rows
F.count()

# Count non-null values
F.count(users.id)

# Unique count
F.uniq(users.id)

# Sum, average, min, max
F.sum(orders.amount)
F.avg(orders.amount)
F.min(metrics.value)
F.max(metrics.value)

# Array aggregation (collect values)
F.groupArray(items.name)

# Conditional aggregation
F.sumIf(orders.amount, orders.status == "completed")
F.countIf(users.id, users.active == 1)
```

#### Aggregate on Entire Table

```py
# Get stats for all records
query = Query(products).aggregate(
    product_count=F.count(),
    avg_price=F.avg(products.price),
    min_price=F.min(products.price),
    max_price=F.max(products.price)
)
# SELECT count() AS product_count, avg(price) AS avg_price, min(price) AS min_price, max(price) AS max_price FROM products
```

### Group

Group rows by one or more columns and optionally aggregate. Produces one row per unique grouping value.

**Critical:** Use the `Aggregate()` wrapper to distinguish aggregate functions from grouping columns. Without it, the expression is treated as a grouping column.

#### Basic Grouping

```py
from pyclickhouse import Aggregate, F

# Group by single column
query = Query(users).group(users.name)
# SELECT name FROM users GROUP BY name

# Group with column alias
query = Query(users).group(user_name=users.name)
# SELECT name AS user_name FROM users GROUP BY name

# Group by multiple columns
query = Query(events).group(
    events.user_id,
    events.event_type
)
# SELECT user_id, event_type FROM events GROUP BY user_id, event_type
```

#### Grouping with Aggregates

```py
# IMPORTANT: Use Aggregate() wrapper to mark aggregate functions
query = Query(orders).group(
    orders.customer_id,
    Aggregate(F.count())
)
# SELECT customer_id, count() FROM orders GROUP BY customer_id

# Named aggregates (REQUIRES Aggregate wrapper)
query = Query(orders).group(
    orders.customer_id,
    total_orders=Aggregate(F.count()),
    total_amount=Aggregate(F.sum(orders.amount))
)
# SELECT customer_id, count() AS total_orders, sum(amount) AS total_amount FROM orders GROUP BY customer_id

# Multiple group columns with multiple aggregates
query = Query(sales).group(
    sales.date,
    sales.region,
    order_count=Aggregate(F.count()),
    total_sales=Aggregate(F.sum(sales.amount)),
    avg_sale=Aggregate(F.avg(sales.amount)),
    max_sale=Aggregate(F.max(sales.amount))
)
# SELECT date, region, count() AS order_count, sum(amount) AS total_sales, avg(amount) AS avg_sale, max(amount) AS max_sale FROM sales GROUP BY date, region
```

#### Grouping with Computed Columns

```py
# Group by derived expressions (functions applied to columns)
query = Query(events).group(
    hour=F.toStartOfHour(events.timestamp),
    event_type=events.type,
    event_count=Aggregate(F.count()),
    unique_users=Aggregate(F.uniq(events.user_id))
)
# SELECT toStartOfHour(timestamp) AS hour, type AS event_type, count() AS event_count, uniq(user_id) AS unique_users
# FROM events GROUP BY toStartOfHour(timestamp), type
```

#### Common Aggregate Functions in Group

```py
# Count
Aggregate(F.count())                              # Total rows
Aggregate(F.count(column))                        # Non-null rows

# Distinct count
Aggregate(F.uniq(column))                         # Unique values

# Sum, average, min, max
Aggregate(F.sum(column))
Aggregate(F.avg(column))
Aggregate(F.min(column))
Aggregate(F.max(column))

# Array aggregation
Aggregate(F.groupArray(column))                   # Collect all values

# Conditional aggregation
Aggregate(F.sumIf(column, condition))
Aggregate(F.countIf(column, condition))
```

#### The Difference: Aggregate vs Group

```py
# aggregate() - one row for entire table
query = Query(orders).aggregate(
    total_orders=F.count(),
    total_amount=F.sum(orders.amount)
)
# SELECT count() AS total_orders, sum(amount) AS total_amount FROM orders

# group() - one row per group, REQUIRES Aggregate() wrapper
query = Query(orders).group(
    orders.customer_id,
    total_orders=Aggregate(F.count()),
    total_amount=Aggregate(F.sum(orders.amount))
)
# SELECT customer_id, count() AS total_orders, sum(amount) AS total_amount FROM orders GROUP BY customer_id
```

#### Group with Window Functions

Apply window functions within a group aggregation using the `Window` class. Window functions compute aggregate values over a subset of rows defined by a range or row count.

```py
from pyclickhouse import Aggregate, Window, F

# Group with window range specification
query = Query(orders).group(
    orders.customer_id,
    total=Aggregate(F.sum(orders.amount)),
    Window(range=(-2, 0))
)
# SELECT customer_id, sum(amount) OVER (RANGE BETWEEN 2 PRECEDING AND CURRENT ROW) AS total FROM orders GROUP BY customer_id

# Group with window rows specification
query = Query(events).group(
    events.date,
    events.type,
    count=Aggregate(F.count()),
    moving_avg=Aggregate(F.avg(events.value)),
    Window(rows=(-3, 0))
)
# SELECT date, type, count() AS count, avg(value) OVER (ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS moving_avg
# FROM events GROUP BY date, type

# Unbounded window (all rows before current row)
query = Query(metrics).group(
    metrics.metric_name,
    cumulative=Aggregate(F.sum(metrics.value)),
    Window(range=(None, 0))
)
# SELECT metric_name, sum(value) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative
# FROM metrics GROUP BY metric_name

# Multiple aggregates with window
query = Query(sales).group(
    sales.region,
    sales.date,
    daily_sales=Aggregate(F.sum(sales.amount)),
    running_total=Aggregate(F.sum(sales.amount)),
    Window(range=(None, 0))
)
# SELECT region, date, sum(amount) AS daily_sales, sum(amount) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
# FROM sales GROUP BY region, date
```

**Window within Group Use Cases:**
- **Running totals** — Cumulative sum with `range=(None, 0)`
- **Moving averages** — Last N rows with `rows=(-N, 0)`
- **Row numbering** — Applied within each group
- **Ranking** — Within grouped partitions

### Window

Create window functions for running totals, moving averages, and row numbering. Window functions compute values based on a subset of rows within a partition.

```py
from pyclickhouse import Window, Aggregate, F

# Window with range specification (default: current row)
query = Query(metrics).window(
    Window(range=(-2, 0)),
    moving_total=Aggregate(F.sum(metrics.value))
)
# SELECT *, sum(value) OVER (RANGE BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_total FROM metrics

# Window with rows specification
query = Query(events).window(
    Window(rows=(-3, 0)),
    moving_avg=Aggregate(F.avg(events.amount))
)
# SELECT *, avg(amount) OVER (ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS moving_avg FROM events

# Unbounded window (all previous rows)
query = Query(sales).window(
    Window(range=(None, 0)),
    cumulative_sales=Aggregate(F.sum(sales.amount))
)
# SELECT *, sum(amount) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_sales FROM sales

# Full window (all rows)
query = Query(data).window(
    Window(range=(None, None)),
    total_percent=Aggregate(F.sum(data.value))
)
# SELECT *, sum(value) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS total_percent FROM data

# Window with current row only
query = Query(records).window(
    Window(rows=(0, 0)),
    current_value=Aggregate(F.sum(records.amount))
)
# SELECT *, sum(amount) OVER (ROWS BETWEEN CURRENT ROW AND CURRENT ROW) AS current_value FROM records
```

#### Range vs Rows

- **Range** — Logical distance based on values (useful for time-based windows)
- **Rows** — Physical distance based on row count

```py
# RANGE BETWEEN: Groups rows by value distance
query = Query(metrics).window(
    Window(range=(-10, 10)),  # ±10 value units
    count=Aggregate(F.count())
)

# ROWS BETWEEN: Groups by row count
query = Query(metrics).window(
    Window(rows=(-10, 10)),  # 10 rows before and after
    count=Aggregate(F.count())
)
```

#### Window Specifications

Values in window tuples:
- **Negative numbers** — PRECEDING (before current row)
- **Positive numbers** — FOLLOWING (after current row)
- **Zero** — CURRENT ROW
- **None** — UNBOUNDED (start/end of partition)

```py
Window(range=(-5, 5))          # 5 before to 5 after
Window(range=(None, 0))        # All previous rows including current
Window(range=(0, None))        # Current row to all following rows
Window(rows=(-10, -1))         # 10 rows before (excluding current)
Window(rows=(1, 10))           # Next 10 rows (excluding current)
Window(rows=(None, None))      # All rows
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

### Example 7: Window Functions - Running Totals

```py
from pyclickhouse import Query, Table, Window, Aggregate, F

class Transaction(BaseModel):
    date: str
    amount: float

transactions = Table(model=Transaction, name="transactions")

# Running total (cumulative sum) across all rows
query = Query(transactions).window(
    Window(range=(None, 0)),
    cumulative_amount=Aggregate(F.sum(transactions.amount))
).sort(transactions.date)

print(str(query))
# SELECT *, sum(amount) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_amount 
# FROM transactions ORDER BY date

# Moving average (average of last 3 rows)
query = Query(transactions).window(
    Window(rows=(-3, 0)),
    moving_avg=Aggregate(F.avg(transactions.amount))
)

print(str(query))
# SELECT *, avg(amount) OVER (ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS moving_avg FROM transactions
```

### Example 8: Group with Window Functions - Per-Group Running Totals

```py
from pyclickhouse import Query, Table, Window, Aggregate, F

class Sale(BaseModel):
    region: str
    date: str
    amount: float

sales = Table(model=Sale, name="sales")

# Running total per region
query = Query(sales).group(
    sales.region,
    sales.date,
    daily_sales=Aggregate(F.sum(sales.amount)),
    region_running_total=Aggregate(F.sum(sales.amount)),
    Window(range=(None, 0))
).sort(sales.region, sales.date)

print(str(query))
# SELECT region, date, sum(amount) AS daily_sales,
#        sum(amount) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS region_running_total
# FROM sales GROUP BY region, date ORDER BY region, date

# Running average within each region (last 5 days)
query = Query(sales).group(
    sales.region,
    sales.date,
    daily_total=Aggregate(F.sum(sales.amount)),
    moving_avg_region=Aggregate(F.avg(sales.amount)),
    Window(rows=(-5, 0))
)

print(str(query))
# SELECT region, date, sum(amount) AS daily_total, avg(amount) OVER (ROWS BETWEEN 5 PRECEDING AND CURRENT ROW) AS moving_avg_region
# FROM sales GROUP BY region, date
```

---

## Aggregate vs Group vs Window

Understanding the differences between these three operations is crucial for writing correct queries.

### Comparison Table

| Feature | `aggregate()` | `group()` | `window()` |
|---------|--------------|----------|-----------|
| **Output rows** | Single row | One per group | One per input row |
| **Use case** | Summarize all data | Summarize per group | Ranking, running totals |
| **Aggregate wrapper** | NO wrapper | YES wrapper | YES wrapper |
| **Partitioning** | Entire table | By GROUP BY columns | Implicit or explicit |
| **Example** | Total sales | Sales per region | Running total per region |

### Aggregate: Summarize Entire Table

`aggregate()` produces a **single row** summarizing all input data. Do NOT use the `Aggregate()` wrapper.

```py
# Count total orders
query = Query(orders).aggregate(F.count())
# SELECT count() FROM orders
# Output: 1 row with total count

# Multiple aggregate metrics
query = Query(orders).aggregate(
    total_orders=F.count(),
    total_amount=F.sum(orders.amount),
    avg_amount=F.avg(orders.amount),
    max_amount=F.max(orders.amount)
)
# SELECT count() AS total_orders, sum(amount) AS total_amount, avg(amount) AS avg_amount, max(amount) AS max_amount FROM orders
# Output: 1 row with all metrics
```

### Group: Summarize by Categories

`group()` produces **one row per unique group**. MUST use the `Aggregate()` wrapper to mark aggregate functions.

```py
# Group by customer (one row per customer)
query = Query(orders).group(
    orders.customer_id,
    total_orders=Aggregate(F.count()),
    total_amount=Aggregate(F.sum(orders.amount))
)
# SELECT customer_id, count() AS total_orders, sum(amount) AS total_amount FROM orders GROUP BY customer_id
# Output: N rows (one per customer)

# Group by date and region
query = Query(sales).group(
    sales.date,
    sales.region,
    daily_sales=Aggregate(F.sum(sales.amount)),
    transaction_count=Aggregate(F.count())
)
# SELECT date, region, sum(amount) AS daily_sales, count() AS transaction_count 
# FROM sales GROUP BY date, region
# Output: N rows (one per unique date+region combination)
```

### Window: Per-Row Aggregates with Context

`window()` produces **one row per input row** with aggregate values computed over a window of rows. MUST use the `Aggregate()` wrapper.

```py
# Running total for each row (cumulative sum)
query = Query(sales).window(
    Window(range=(None, 0)),
    running_total=Aggregate(F.sum(sales.amount))
)
# SELECT *, sum(amount) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total FROM sales
# Output: Same number of rows as input, with running total

# Moving average (last 3 rows)
query = Query(metrics).window(
    Window(rows=(-3, 0)),
    moving_avg=Aggregate(F.avg(metrics.value))
)
# SELECT *, avg(value) OVER (ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS moving_avg FROM metrics
# Output: Same number of rows as input, with moving average
```

### Group with Window: Grouped Running Totals

Combine `group()` with `Window()` to get running totals **per group**:

```py
# Running total per customer
query = Query(orders).group(
    orders.customer_id,
    order_amount=Aggregate(F.sum(orders.amount)),
    cumulative=Aggregate(F.sum(orders.amount)),
    Window(range=(None, 0))
)
# SELECT customer_id, sum(amount) AS order_amount, 
#        sum(amount) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative
# FROM orders GROUP BY customer_id
# Output: One row per customer with daily amount and running total

# Hourly sales with daily running total
query = Query(sales).group(
    sales.date,
    sales.hour,
    hourly_sales=Aggregate(F.sum(sales.amount)),
    daily_running_total=Aggregate(F.sum(sales.amount)),
    Window(range=(None, 0))
)
# SELECT date, hour, sum(amount) AS hourly_sales,
#        sum(amount) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS daily_running_total
# FROM sales GROUP BY date, hour
# Output: One row per hour, with cumulative total within each day
```

### Side-by-Side Example

```py
from pyclickhouse import Query, Table, F, Aggregate, Window
from pydantic import BaseModel

class Sale(BaseModel):
    date: str
    amount: float

sales = Table(model=Sale, name="sales")

# 1. Aggregate: Total across all days
q1 = Query(sales).aggregate(
    total_sales=F.sum(sales.amount)
)
# Output: | total_sales |
#         | 1000        |

# 2. Group: Total per day
q2 = Query(sales).group(
    sales.date,
    daily_sales=Aggregate(F.sum(sales.amount))
)
# Output: | date       | daily_sales |
#         | 2024-01-01 | 100         |
#         | 2024-01-02 | 150         |
#         | 2024-01-03 | 250         |

# 3. Window: Each row with running total
q3 = Query(sales).window(
    Window(range=(None, 0)),
    cumulative=Aggregate(F.sum(sales.amount))
)
# Output: | date       | amount | cumulative |
#         | 2024-01-01 | 100    | 100        |
#         | 2024-01-02 | 150    | 250        |
#         | 2024-01-03 | 250    | 500        |

# 4. Group + Window: Per-day running total
q4 = Query(sales).group(
    sales.date,
    Aggregate(F.sum(sales.amount)),
    Window(range=(None, 0))
)
# Output: | date       | sum(amount) | sum(...) OVER (...) |
#         | 2024-01-01 | 100         | 100                 |
#         | 2024-01-02 | 150         | 250                 |
#         | 2024-01-03 | 250         | 500                 |
```

---

## Learn More

- [PRQL Documentation](https://prql-lang.org/) — Learn about PRQL language features
- [ClickHouse Functions](https://clickhouse.com/docs/sql-reference/functions) — Complete function reference
- [Reader](/concepts/reader) — Execute queries and retrieve results
- [Table](/concepts/table) — Define tables and access columns
- [View](/concepts/view) — Create and manage views
