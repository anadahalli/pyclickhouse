from datetime import date, datetime, time, timedelta
from typing import Any

TYPE_MAPPING: dict[type, str] = {
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


def get_default_type(field_type: Any | type[Any]) -> str:
    return TYPE_MAPPING.get(field_type, "String")
