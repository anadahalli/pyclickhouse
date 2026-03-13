from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from ipaddress import IPv4Address, IPv6Address
from types import NoneType
from typing import Any, Dict, List, Literal, Optional, Tuple
from uuid import UUID

import pytest

from pyclickhouse.types import (
    get_ch_type_from_annotation,
    get_python_type_from_ch_string,
)

py_type_to_ch_type = [
    # primitive types
    (str, "String"),
    (int, "Int64"),
    (float, "Float64"),
    (bool, "Bool"),
    (date, "Date"),
    (datetime, "DateTime"),
    (Decimal, "Decimal"),
    (UUID, "UUID"),
    (IPv4Address, "IPv4"),
    (IPv6Address, "IPv6"),
    # optional primitive types
    (str | None, "Nullable(String)"),
    (int | None, "Nullable(Int64)"),
    (float | None, "Nullable(Float64)"),
    (bool | None, "Nullable(Bool)"),
    (date | None, "Nullable(Date)"),
    (datetime | None, "Nullable(DateTime)"),
    (UUID | None, "Nullable(UUID)"),
    (IPv4Address | None, "Nullable(IPv4)"),
    (IPv6Address | None, "Nullable(IPv6)"),
    (Decimal | None, "Nullable(Decimal)"),
    # union primitive types
    (str | int, "Variant(String, Int64)"),
    (str | int | float, "Variant(String, Int64, Float64)"),
    (str | int | None, "Dynamic"),
    # list
    (list[str], "Array(String)"),
    (list[int], "Array(Int64)"),
    (list[float], "Array(Float64)"),
    (list[str | None], "Array(Nullable(String))"),
    (list[int | float], "Array(Variant(Int64, Float64))"),
    (list[int | float | None], "Array(Dynamic)"),
    (List[Optional[str]], "Array(Nullable(String))"),
    (list, "Array(Dynamic)"),
    # tuple
    (tuple[str], "Tuple(String)"),
    (tuple[str | None], "Tuple(Nullable(String))"),
    (tuple[str | int], "Tuple(Variant(String, Int64))"),
    (tuple[str | int | None], "Tuple(Dynamic)"),
    (Tuple[Optional[str]], "Tuple(Nullable(String))"),
    (tuple, "Tuple(Dynamic)"),
    # dict
    (dict[str, str], "Map(String, String)"),
    (dict[str, int], "Map(String, Int64)"),
    (dict[str, int | None], "Map(String, Nullable(Int64))"),
    (Dict[str, Optional[str]], "Map(String, Nullable(String))"),
    (dict, "JSON"),
    # Literal
    (Literal["a"], "Enum('a')"),
    # Enum
    (Enum("e", names=("1", "2")), "Enum('1', '2')"),
    # NoneType
    (NoneType, "Dynamic"),
    # Nested
]


@pytest.mark.parametrize("py_type,ch_type", py_type_to_ch_type)
def test_get_ch_type_from_annotation(py_type: type, ch_type: str) -> None:
    assert get_ch_type_from_annotation(py_type) == ch_type


ch_type_to_py_type = [
    ("Bool", bool),
    ("Int8", int),
    ("Int256", int),
    ("UInt8", int),
    ("Float32", float),
    ("Float64", float),
    ("Decimal", float),
    ("String", str),
    ("DateTime64(3)", datetime),
    ("Date", date),
    ("FixedString", str),
    ("Nullable(String)", str | None),
    ("Array(String)", list),
    ("Array(Nullable(String))", list),
    ("Tuple(String)", tuple),
    ("Map(String, String)", dict),
    ("Variant(String, String)", Any),
    ("Enum", str),
    ("Dynamic", Any),
]


@pytest.mark.parametrize("ch_string,py_type", ch_type_to_py_type)
def test_get_python_type_from_ch_string(ch_string: str, py_type: type) -> None:
    assert get_python_type_from_ch_string(ch_string) == py_type
