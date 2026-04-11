import types
import typing
from datetime import date, datetime
from decimal import Decimal
from enum import EnumType, StrEnum, auto
from ipaddress import IPv4Address, IPv6Address
from typing import Any
from uuid import UUID


def get_ch_type_from_annotation(annotation: Any | None | type[Any]) -> str:
    primitive_map: dict[type, str] = {
        str: "String",
        int: "Int64",
        float: "Float64",
        bool: "Bool",
        date: "Date",
        datetime: "DateTime",
        Decimal: "Decimal",
        UUID: "UUID",
        IPv4Address: "IPv4",
        IPv6Address: "IPv6",
        # type(None): "Nothing",
    }

    # primitive types -> T
    if annotation in primitive_map:
        return primitive_map[annotation]

    origin = typing.get_origin(annotation)
    args = typing.get_args(annotation)
    # print(annotation, origin, args)

    # union types -> Nullable(T) or or Dyanmic or Variant(T1, T2, ...)
    if origin is typing.Union or origin is types.UnionType:
        non_none_args = [a for a in args if not (a is None or a is type(None))]
        if len(non_none_args) == 1:
            inner_type = get_ch_type_from_annotation(non_none_args[0])
            return f"Nullable({inner_type})"
        if len(args) > len(non_none_args):
            return "Dynamic"
        inner_types = ", ".join(get_ch_type_from_annotation(a) for a in non_none_args)
        return f"Variant({inner_types})"

    # list -> Array(T)
    if annotation is list or annotation is typing.List:
        return "Array(Dynamic)"
    if origin is list or origin is typing.List:
        inner_type = get_ch_type_from_annotation(args[0])
        return f"Array({inner_type})"

    # tuple -> Tuple(T1, T2, ...)
    if annotation is tuple or annotation is typing.Tuple:
        return "Tuple(Dynamic)"
    if origin is tuple or origin is typing.Tuple:
        inner_types = ", ".join(get_ch_type_from_annotation(a) for a in args)
        return f"Tuple({inner_types})"

    # dict -> Map(K, V)
    if annotation is dict or annotation is typing.Dict:
        # return "Map(Dynamic, Dynamic)"
        return "JSON"
    if origin is dict or origin is typing.Dict:
        key_type = get_ch_type_from_annotation(args[0])
        value_type = get_ch_type_from_annotation(args[1])
        return f"Map({key_type}, {value_type})"

    # Enum -> Enum(keys)
    if type(annotation) is EnumType:
        keys = ", ".join(f"'{getattr(m, 'name')}'" for m in list(annotation))
        return f"Enum({keys})"

    # Literal -> Enum(args)
    if origin is typing.Literal or origin is typing.LiteralString:
        keys = ", ".join(f"'{v}'" for v in args)
        return f"Enum({keys})"

    return "Dynamic"


def get_python_type_from_ch_string(ch_type: str) -> type | Any:
    type_map: dict[str, type] = {
        "Int": int,
        "UInt": int,
        "Float": float,
        "Decimal": float,
        "String": str,
        "FixedString": str,
        "UUID": str,
        "Bool": bool,
        "Date": date,
        "DateTime": datetime,
        "Array": list,
        "Map": dict,
        "Tuple": tuple,
        "Enum": str,
        "Dynamic": Any,
    }

    # handle Nullable wrapper
    if ch_type.startswith("Nullable("):
        inner_type = ch_type[9:-1]
        py_type = get_python_type_from_ch_string(inner_type)
        return typing.Optional[py_type]  # type: ignore

    # handle LowCardinality wrapper
    if ch_type.startswith("LowCardinality("):
        inner_type = ch_type[15:-1]
        return get_python_type_from_ch_string(inner_type)

    # sort keys by length (descending) to ensure "DateTime64" matches before "Date", etc
    type_map_items = sorted(type_map.items(), key=lambda x: len(x[0]), reverse=True)

    for prefix, py_type in type_map_items:
        if ch_type.startswith(prefix):
            return py_type

    return Any


class Lifecycle(StrEnum):
    managed = auto()
    protected = auto()
    external = auto()
