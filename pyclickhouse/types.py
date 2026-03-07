from abc import ABC
from datetime import date, datetime, time, timedelta
from typing import Any, ClassVar, Self

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

CLICKHOUSE_TO_PYTHON: dict[str, type] = {
    "String": str,
    "Int32": int,
}


def get_clickhouse_type(field_type: Any | type[Any]) -> str:
    return PYTHON_TO_CLICKHOUSE.get(field_type, "String")


def get_python_type(return_type: str) -> type:
    return CLICKHOUSE_TO_PYTHON.get(return_type, str)


class ClickHouseType(ABC):
    base_type: ClassVar[str]
    python_type: ClassVar[type]

    def __init_subclass__(cls, registered: bool = True) -> None:
        if registered:
            cls.base_type = cls.__name__
            type_map[cls.base_type] = cls

    def __init__(self, inner_type: Self | None = None) -> None:
        self.inner_type = inner_type

    def __str__(self) -> str:
        return self.to_sql()

    def to_sql(self) -> str:
        if self.inner_type:
            return f"{self.base_type}({str(self.inner_type)})"
        return self.base_type


type_map: dict[str, type[ClickHouseType]] = {}


class StringType(ClickHouseType, ABC, registered=False):
    python_type = str


class IntType(ClickHouseType, ABC, registered=False):
    python_type = int


class FloatType(ClickHouseType, ABC, registered=False):
    python_type = float


class BoolType(ClickHouseType, ABC, registered=False):
    python_type = bool


class DateType(ClickHouseType, ABC, registered=False):
    python_type = date


class TimeType(ClickHouseType, ABC, registered=False):
    python_type = time


class DateTimeType(ClickHouseType, ABC, registered=False):
    python_type = datetime


class ContainerType(ClickHouseType, ABC, registered=False):
    pass


# String
class String(StringType):
    pass


# FixedString
class FixedString(StringType):
    pass


# Numeric
# Int8
# ...
# BigInt
# Float
# ...
# Boolean
# Enum
# ...
# Decimal
# ...
# BigDecimal
# Interval
# ...

# Bool

# Temporal
# Date
# Date32
# DateTime
# DateTime64
# Time
# Time64


# Container
# Array
# Tuple
# Map
# Nested


class LowCardinality(ContainerType):
    python_type = str


# Network
# IPv4
# IPv6

# Special
# UUID
# JSON
