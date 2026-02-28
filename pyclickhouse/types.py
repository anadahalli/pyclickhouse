from datetime import date, datetime, time, timedelta
from typing import Any

PYTHON_TO_CLICKHOUSE: dict[type, str] = {
    int: "Int32",
    str: "String",
    float: "Float64",
    bool: "Bool",
    datetime: "DateTime",
    date: "Date",
    time: "Time",
    timedelta: "Interval",
    Any: "String",
}


def get_clickhouse_type(field_type: Any | type[Any]) -> str:
    return PYTHON_TO_CLICKHOUSE.get(field_type, "String")


CLICKHOUSE_TO_PYTHON: dict[str, type] = {
    "String": str,
    "Int32": int,
}


def get_python_type(return_type: str) -> type:
    return CLICKHOUSE_TO_PYTHON.get(return_type, str)
