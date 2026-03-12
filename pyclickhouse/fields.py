from dataclasses import KW_ONLY, dataclass
from typing import Any, Callable, Self

from pydantic.fields import FieldInfo

from .types import get_clickhouse_type
from .utils import escape


@dataclass
class Column:
    """
    ClickHouse column.

    Args:
        type: The ClickHouse type of the column.
        name: The name of the column.
        default_type: The default type of the column.
        default_expression: The default expression of the column.
        comment: The comment of the column.
        codec_expression: The codec expression of the column.
        ttl_expression: The TTL expression of the column.

    Examples:
        >>> Column(type="String", name="name")
        Column(type='String', name='name', default_type='', default_expression='', comment='', codec_expression='', ttl_expression='')
    """

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
        """
        Create a `Column` instance from a `pydantic.Field`.

        Args:
            name: Name of the column.
            info: `pydantic.FieldInfo` instance.
        """

        meta = [col for col in info.metadata if isinstance(col, Column)]
        column = meta[0] if meta else cls()
        if not column.name:
            column.name = name
        if not column.type:
            column.type = get_clickhouse_type(info.annotation)
        return column

    @classmethod
    def from_sql(cls, **kwargs: Any) -> Self:
        """
        Create a `Column` instance from a SQL column definition.

        Args:
            **kwargs: Column definition keyword arguments.
        """
        return cls(**kwargs)

    def to_sql(self) -> str:
        """
        Convert the column to a SQL column definition.

        Returns:
            SQL column definition as a string.
        """
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
    """
    ClickHouse Query expression with support for different operations.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    # def to_sql(self) -> str:
    #     if self._other is not None and self._operator is not None:
    #         value = str(self._value)
    #         operator = self._operator
    #         if isinstance(self._other, Param):
    #             other = str(self._other)
    #         elif isinstance(self._other, str):
    #             other = f"'{self._other}'"
    #         else:
    #             other = str(self._other)
    #         return f"{value} {operator} {other}"
    #     elif self._prefix is not None:
    #         return f"{self._prefix}{str(self._value)}"
    #     return str(self._value)

    def __str__(self) -> str:
        return str(self.value)

    def _operation(self, operator: str, other: Any) -> Self:
        return type(self)(f"{str(self.value)} {operator} {str(escape(other))}")

    def _prefixer(self, prefix: str) -> Self:
        return type(self)(f"{prefix}{str(self.value)}")

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

    # logical operators: and, or, invert
    def __and__(self, other: Any) -> Self:
        return self._operation("&&", other)

    def __or__(self, other: Any) -> Self:
        return self._operation("||", other)

    def __invert__(self) -> Self:
        return self._prefixer("!")

    # unary operators: neg, pos
    def __neg__(self) -> Self:
        return self._prefixer("-")

    def __pos__(self) -> Self:
        return self._prefixer("+")

    # containes
    def is_in(self, other: Any) -> Self:
        return type(self)(f"({str(self.value)} | in {str(other)})")

    def is_not_in(self, other: Any) -> Self:
        return type(self)(f"!({str(self.value)} | in {str(other)})")


class Param:
    """
    ClickHouse parameter used in queries for parameterized values.

    Args:
        name: Name of the parameter.
        type: ClickHouse type.

    Examples:
        >>> Param("name", str)
        Param(name, str)
    """

    def __init__(self, name: str, type: type = str) -> None:
        self.name = name
        self.type = get_clickhouse_type(type)

    def __str__(self) -> str:
        value = f"{self.name}:{self.type}"
        return "s'{{" + value + "}}'"


class Function:
    def __init__(self, value: str | "Function") -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def to_sql(self) -> str:
        if isinstance(self.value, Function):
            return str(self.value)
        return f"s'{str(self.value)}'"


class Aggregate:
    def __init__(self, value: str | Function) -> None:
        self.value = value

    def __str__(self) -> str:
        if isinstance(self.value, Function):
            return self.value.to_sql()
        return str(self.value)


class FunctionWrapper:
    """ClickHouse function"""

    def __getattr__(self, name: str) -> Callable[..., Function]:
        def wrapper(*args: Any) -> Function:
            params = ", ".join(map(str, args))
            return Function(f"{name}({params})")

        return wrapper


F = FunctionWrapper()
