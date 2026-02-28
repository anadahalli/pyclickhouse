from dataclasses import KW_ONLY, dataclass, field
from typing import Any, Self

from pydantic.fields import FieldInfo

from .types import get_clickhouse_type


@dataclass
class Column:
    type: str | None = None
    name: str | None = None

    _: KW_ONLY

    # nullable [NULL | NOT NULL]
    nullable: bool | None = None

    # default values [DEFAULT|MATERIALIZED|EPHEMERAL|ALIAS expr]
    default: str | None = None
    materialized: str | None = None
    alias: str | None = None
    # ephemeral: bool = False

    # codec [compression_codec]
    codec: str | None = None

    # ttl [TTL expr]
    ttl: str | None = None

    # [COMMENT str]
    comment: str | None = None

    _name: str | None = field(
        default=None,
        init=False,
        repr=False,
        compare=False,
    )
    _field: FieldInfo | None = field(
        default=None,
        init=False,
        repr=False,
        compare=False,
    )
    _read_only: bool = field(
        default=False,
        init=False,
        repr=False,
        compare=False,
    )

    @classmethod
    def from_field(cls, name: str, field: FieldInfo) -> Self:
        column = next((col for col in field.metadata if isinstance(col, Column)), None)

        if column is None:
            column = cls()

        column._name = name
        column._field = field

        if column.type is None:
            column.type = get_clickhouse_type(field.annotation)

        if column.name is None:
            column.name = name

        return column

    def __post_init__(self):
        if not [self.default, self.materialized, self.alias].count(None) >= 2:
            raise TypeError(
                "Column can only have one of default, materialized, or alias"
            )

    def get_type(self) -> str:
        if self.type is None:
            raise TypeError("Column is missing type")
        return self.type

    def get_name(self) -> str:
        if self.name is None:
            raise TypeError("Column is missing name")
        return self.name

    def to_sql(self) -> str:
        parts: list[str] = [f"{self.get_name()} {self.get_type()}"]

        if self.nullable is not None:
            parts.append("NULL" if self.nullable else "NOT NULL")

        if self.default is not None:
            parts.append(f"DEFAULT {self.default}")
        elif self.materialized is not None:
            parts.append(f"MATERIALIZED {self.materialized}")
        elif self.alias is not None:
            parts.append(f"ALIAS {self.alias}")

        if self.comment is not None:
            parts.append(f"COMMENT '{self.comment}'")

        if self.codec is not None:
            parts.append(f"CODEC({self.codec})")

        if self.ttl is not None:
            parts.append(f"TTL {self.ttl}")

        return " ".join(parts).strip()

    def __str__(self) -> str:
        return self.get_name()

    # comparision operators: lt, le, gt, ge, eq, ne
    def __lt__(self, other: Any) -> str:
        return f"{self.get_name()} < {other}"

    def __le__(self, other: Any) -> str:
        return f"{self.get_name()} <= {other}"

    def __gt__(self, other: Any) -> str:
        return f"{self.get_name()} > {other}"

    def __ge__(self, other: Any) -> str:
        return f"{self.get_name()} >= {other}"

    def __eq__(self, other: Any) -> str:  # type: ignore
        value = other
        if isinstance(other, str):
            value = f'"{value}"'
        return f"{self.get_name()} == {value}"

    def __ne__(self, other: Any) -> str:  # type: ignore
        value = other
        if isinstance(other, str):
            value = f'"{value}"'
        return f"{self.get_name()} != {value}"

    # airthmetic operators: add, sub, etc
    def __add__(self, other: Any) -> str:
        return f"{self.get_name()} + {other}"

    def __sub__(self, other: Any) -> str:
        return f"{self.get_name()} - {other}"

    def __mul__(self, other: Any) -> str:
        return f"{self.get_name()} * {other}"

    def __truediv__(self, other: Any) -> str:
        return f"{self.get_name()} / {other}"

    # logical operators: and, or, invert, contains
    def __contains__(self, other: Any) -> str:
        return f"{self.get_name()} IN {other}"

    def __and__(self, other: Any) -> str:
        return f"{self.get_name()} AND {other}"

    def __or__(self, other: Any) -> str:
        return f"{self.get_name()} OR {other}"

    def __invert__(self) -> str:
        return f"NOT {self.get_name()}"


class Constraint:
    pass


class Index:
    pass
