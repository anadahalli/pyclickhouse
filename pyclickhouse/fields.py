from dataclasses import KW_ONLY, dataclass
from typing import Any, Callable, Self

from pydantic.fields import FieldInfo

from .types import get_clickhouse_type


@dataclass
class Column:
    type: str = ""
    name: str = ""
    _: KW_ONLY
    default_type: str = ""
    default_expression: str = ""
    comment: str = ""
    codec_expression: str = ""
    ttl_expression: str = ""

    @classmethod
    def from_field(cls, name: str, info: FieldInfo) -> Self:
        meta = [col for col in info.metadata if isinstance(col, Column)]
        column = meta[0] if meta else cls()
        if not column.name:
            column.name = name
        if not column.type:
            column.type = get_clickhouse_type(info.annotation)
        return column

    @classmethod
    def from_sql(cls, **kwargs: Any) -> Self:
        return cls(**kwargs)

    def to_sql(self) -> str:
        parts: list[str] = []
        if not self.name:
            raise ValueError("name is required")
        parts.append(self.name)
        if not self.type:
            raise ValueError("type is required")
        parts.append(str(self.type))
        if self.default_type:
            if not self.default_expression:
                raise ValueError("default_expression is required for default_type")
            parts.append(f"{self.default_type} {self.default_expression}")
        if self.comment:
            parts.append(f"COMMENT '{self.comment}'")
        if self.codec_expression:
            parts.append(f"CODEC({self.codec_expression})")
        if self.ttl_expression:
            parts.append(f"TTL {self.ttl_expression}")
        return " ".join(parts)

    def __str__(self) -> str:
        return self.name


class Expression:
    def __init__(self, value: str | Column | "Expression") -> None:
        self._value = value
        self._other: str | Column | None = None
        self._operator: str | None = None
        self._prefix: str | None = None

    @property
    def value(self) -> str:
        if self._other is not None and self._operator is not None:
            value = str(self._value)
            operator = self._operator
            if isinstance(self._other, str):
                other = f"'{self._other}'"
            else:
                other = str(self._other)
            return f"{value} {operator} {other}"
        elif self._prefix is not None:
            return f"{self._prefix}{str(self._value)}"
        return str(self._value)

    def to_sql(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value

    def _operation(self, operator: str, other: Any) -> Self:
        self._operator = operator
        self._other = other
        return self

    def _prefixer(self, prefix: str) -> Self:
        self._prefix = prefix
        return self

    # comparision operators: lt, le, gt, ge, eq, ne
    def __lt__(self, other: Any) -> Self:
        return self._operation("<", other)

    def __le__(self, other: Any) -> Self:
        return self._operation("<=", other)

    def __gt__(self, other: Any) -> Self:
        return self._operation(">", other)

    def __ge__(self, other: Any) -> Self:
        return self._operation(">=", other)

    def __eq__(self, other: Any) -> Self:  # type: ignore
        return self._operation("==", other)

    def __ne__(self, other: Any) -> Self:  # type: ignore
        return self._operation("!=", other)

    # airthmetic operators: add, sub, etc
    def __add__(self, other: Any) -> Self:
        return self._operation("+", other)

    def __sub__(self, other: Any) -> Self:
        return self._operation("-", other)

    def __mul__(self, other: Any) -> Self:
        return self._operation("*", other)

    def __truediv__(self, other: Any) -> Self:
        return self._operation("/", other)

    # logical operators: and, or, invert, contains
    def __contains__(self, other: Any) -> str:
        return f"{self.value} IN {other}"

    def __and__(self, other: Any) -> str:
        return f"{self.value} && {other}"

    def __or__(self, other: Any) -> str:
        return f"{self.value} || {other}"

    def __invert__(self) -> Self:
        return self._prefixer("!")

    # unary operators: neg, pos, abs
    def __neg__(self) -> Self:
        return self._prefixer("-")

    def __pos__(self) -> Self:
        return self._prefixer("+")


class Function:
    def __getattr__(self, name: str) -> Callable[..., Expression]:
        def wrapper(*args: Any) -> Expression:
            params = ", ".join(map(str, args))
            value = f"s'{name}({params})'"
            return Expression(value)

        return wrapper


F = Function()


class Aggregate:
    def __init__(self, value: str | Expression) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)
