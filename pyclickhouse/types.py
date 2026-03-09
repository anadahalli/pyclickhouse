from datetime import date, datetime, time, timedelta
from enum import StrEnum, auto
from typing import Any

type_map: dict[type, str] = {
    int: "Int32",
    str: "String",
    float: "Float64",
    bool: "Bool",
    datetime: "DateTime",
    date: "Date",
    time: "Time",
    timedelta: "Interval",
    dict: "JSON",
}


def get_clickhouse_type(field_type: Any | type[Any]) -> str:
    return type_map.get(field_type, "String")


# from clickhouse types to python type
prefix_map: dict[str, type] = {
    # Boolean
    "Bool": bool,
    # Int
    "Int": int,
    "UInt": int,
    # Float
    "Float": float,
    # Decimal
    "Decimal": float,
    # String
    "String": str,
    "FixedString": str,
    # Temporal
    "DateTime": datetime,
    "Date": date,
    "Time": time,
    # Enum
    # UUID
    # Network
    # Special
    "JSON": dict,
}


def get_python_type(return_type: str) -> type:
    for prefix, py_type in prefix_map.items():
        if return_type.startswith(prefix):
            return py_type

    return str


class Lifecycle(StrEnum):
    managed = auto()
    protected = auto()
    external = auto()
