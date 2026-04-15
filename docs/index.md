# Overview

A modern async Python ORM for ClickHouse
___

## Features
* Async first design: non-blocking API built around async/await using `clickhouse_connect`
* Data models: using `pydantic` models for table design, serialization and deserialization with auto data types
* Query builder: build expressive and composable queries using `prql`
* Database admin: create and manage tables/views and migrations
* Batch writer: Validate and insert data in batches to tables
* Stream reader: Parameterize queries and deserialize results with support for streaming

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

## Next

Explore [Concepts](/concepts/client)

Browse [References](/references/client)
