# Overview

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

## Quickstart

```py
--8<-- "./examples/quickstart.py"
```

---

## Explore

Read [Concepts](/concepts/client)

Check [Examples](https://github.com/anadahalli/pyclickhouse/tree/main/examples)

API [References](/references/client)

---

## License
[MIT License](https://github.com/anadahalli/pyclickhouse/blob/main/LICENSE)
