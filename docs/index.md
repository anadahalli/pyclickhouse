---
title: Overview
---

A modern async Python ORM for ClickHouse using Pydantic.

## Features

* **Async** HTTP client using `clickhouse_connect`
* **Model** data using `pydantic` for tables with auto data types
* **Query** builder using `prql` to create composable queries
* **Admin** to create and manage tables/views and migrations
* **Writer** to validate and insert data in batches to tables
* **Reader** to query and stream results with validation

---

## Installation

=== "uv"
    ```sh
    uv add pyclickhouse
    ```
=== "pip"
    ```sh
    pip install pyclickhouse
    ```
=== "source"
    ```sh
    uv add git+https://github.com/anadahalli/pyclickhouse.git
    ```

---

## Quick Start

```py
--8<-- "./examples/quickstart.py"
```

---

## Core Concepts

Learn the core concepts and how to use PyClickHouse:

- **[Client](/concepts/client/)** — Connect to ClickHouse and manage the async connection lifecycle. Learn how to initialize clients, execute queries directly, and manage database connections.

- **[Table](/concepts/table/)** — Define ClickHouse tables from Pydantic models. Map Python types to ClickHouse columns, customize table names and types, manage table lifecycle and auto-registration with the registry.

- **[Query](/concepts/query/)** — Build type-safe, composable queries using PRQL. Filter, select, aggregate, group, join, and apply window functions. Use parameterized queries for dynamic SQL generation.

- **[View](/concepts/view/)** — Create simple views (virtual queries) and materialized views (persisted results). Understand view lifecycle, auto-registration, and patterns for incremental data loading and denormalization.

- **[Reader](/concepts/reader/)** — Execute queries and retrieve results. Query with parameters, stream results asynchronously, and iterate over rows with automatic validation.

- **[Writer](/concepts/writer/)** — Insert validated data in batches. Create writers for efficient bulk inserts, manage batch sizing and flushing, and track written rows.

- **[Admin](/concepts/admin/)** — Manage the database schema. Create, alter, and drop tables/views, perform migrations with lifecycle awareness, introspect existing tables, and bulk operations.

## Use Cases

#### I want to query data
Start with [Client](/concepts/client/) to understand how to connect, then move to [Query](/concepts/query/) to learn how to build queries, and finally [Reader](/concepts/reader/) to execute them and get results.

#### I want to insert data
Create a Pydantic model and [Table](/concepts/table/) definition, then use [Writer](/concepts/writer/) to insert data in batches.

#### I want to manage schema
Use [Admin](/concepts/admin/) to create tables from Pydantic models, perform migrations with lifecycle controls, and manage views. See [Table](/concepts/table/) and [View](/concepts/view/) for schema design patterns.

#### I want to transform data
Use [View](/concepts/view/) to create materialized views that compute and store results, combined with [Query](/concepts/query/) to define the transformation logic.

---

## Examples

### Define a Table

```py
from pydantic import BaseModel
from pyclickhouse import Table

class User(BaseModel):
    id: int
    name: str
    email: str

users = Table(model=User, name="users")
```

### Build a Query

```py
from pyclickhouse import Query, F

query = Query(users).filter(
    users.id > 10
).select(
    users.name,
    users.email
)
```

### Insert Data

```py
from pyclickhouse import Writer

async with client:
    writer = Writer(client, users)
    writer.write(User(id=1, name="Alice", email="alice@example.com"))
    await writer.flush()
```

### Execute a Query

```py
from pyclickhouse import Reader

async with client:
    reader = Reader(client, query)
    results = await reader.query()
    for row in results:
        print(row)
```

### Create a Table

```py
from pyclickhouse import Admin

async with client:
    admin = Admin(client)
    await admin.create_table(users)
```

### Create a Materialized View

```py
from pyclickhouse import View

high_value_sales = View(
    name="high_value_sales",
    query=Query(sales).filter(sales.amount > 1000),
    table=Table(model=SaleSummary, name="high_value_sales_storage")
)

async with client:
    admin = Admin(client)
    await admin.create_view(high_value_sales)
```

---

## Key Features

### Query Builder
- **PRQL-based** — Compose queries using pipeline operations, compiling to ClickHouse SQL
- **Type-safe** — Column references are typed via Pydantic models
- **Composable** — Chain operations like filter, select, aggregate, group, sort, take
- **Parameterized** — Support runtime parameters with automatic type inference
- **Functions** — Access 1000+ ClickHouse functions via the `F` object
- **Advanced** — Join tables and compute window functions (planned features with documented APIs)

### Table & Schema
- **Auto-typed** — Python types automatically mapped to ClickHouse types
- **Customizable** — Override column names and types; add defaults, comments, codecs
- **Lifecycle-aware** — Mark tables as `managed`, `protected`, or `external` to control migrations
- **Auto-registered** — Tables register with a global registry by default
- **Reflection** — Introspect existing tables from ClickHouse and generate Pydantic models

### Views
- **Simple views** — Virtual tables executing queries on-demand
- **Materialized views** — Persist computed results with automatic updates from source tables
- **Integration** — Kafka and PostgreSQL engines for streaming and federated data
- **Patterns** — Built-in support for incremental loading, denormalization, and aggregation

### Admin & Migrations
- **Create/Alter/Drop** — Full DDL support for tables and views
- **Lifecycle-aware** — Respect `managed`/`protected`/`external` lifecycle tags during migrations
- **Bulk operations** — `create_all()` and `migrate_all()` for multiple tables at once
- **Introspection** — `get_table()` to reflect existing ClickHouse tables as Pydantic models

### Reader & Writer
- **Async streaming** — Non-blocking iteration over query results
- **Validation** — Automatic Pydantic validation of data in and out
- **Batching** — Efficient bulk inserts with configurable batch sizes
- **Parameters** — Pass runtime values to parameterized queries

---

## Explore Further

- **[Examples](https://github.com/anadahalli/pyclickhouse/tree/main/examples)** — Working code samples for common patterns
- **[API References](/references/client/)** — Detailed API documentation for all classes and methods
- **[GitHub](https://github.com/anadahalli/pyclickhouse)** — Source code, issues, and contributions

---

## Development

### Local Setup

To set up the development environment:

```sh
# Clone the repository
git clone https://github.com/anadahalli/pyclickhouse.git
cd pyclickhouse

# Install development dependencies
uv sync --group dev
```

### Running Tests

Execute the test suite with:

```sh
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=pyclickhouse

# Run a specific test file
uv run pytest tests/test_client.py
```

### Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

Please ensure your code follows the project's style and includes tests for new functionality.

### Issues and Feedback

- **Bug Reports**: Please open an issue on [GitHub Issues](https://github.com/anadahalli/pyclickhouse/issues) with a clear description and steps to reproduce
- **Feature Requests**: Submit feature requests through GitHub Issues
- **Questions**: Use GitHub Discussions or open an issue for general questions
- **Feedback**: We appreciate any feedback! Feel free to reach out through GitHub Issues

---

## License

[MIT License](https://github.com/anadahalli/pyclickhouse/blob/main/LICENSE)