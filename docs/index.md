# Overview

A modern async Python ORM for ClickHouse

---

## Features
* Async first design: non-blocking API built around async/await
* Pluggable drivers: choose between `clickhouse-connect` or `asynch`
* Typed models: Define schemas with `pydantic` models for validation and serialization
* Database management: create and manage tables/views
* Query builder: build expressive and composable queries using `prql`
* Batch writer: Validate and insert data in batches

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

## Roadmap

* Support complex datatypes: Nested, Array, Tuple, JSON
* Support table joins and windows
* Support for file based migrations

---

## License
[MIT License](LICENSE)
