from datetime import date, datetime

import pytest

from pyclickhouse.types import get_clickhouse_type, get_python_type  # noqa


@pytest.mark.parametrize(
    "py_type,ch_string",
    [
        (int, "Int32"),
        (str, "String"),
        (float, "Float64"),
        (bool, "Bool"),
        (datetime, "DateTime"),
        (date, "Date"),
    ],
)
def test_get_clickhouse_types(py_type: type, ch_string: str) -> None:
    assert get_clickhouse_type(py_type) is ch_string


@pytest.mark.parametrize(
    "ch_string,py_type",
    [
        ("Bool", bool),
        ("Int8", int),
        ("Int256", int),
        ("UInt8", int),
        ("Float32", float),
        ("Float64", float),
        ("Decimal", float),
        ("String", str),
        ("FixedString", str),
    ],
)
def test_get_python_types(ch_string: str, py_type: type) -> None:
    assert get_python_type(ch_string) is py_type
