from typing import Any

from .column import Column


class Expression:
    def __init__(self, value: str | Column | "Expression") -> None:
        self._value = value

    @property
    def value(self) -> str:
        if isinstance(self._value, Column):
            return self._value.get_name()
        return str(self._value)

    def to_sql(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value

    # comparision operators: lt, le, gt, ge, eq, ne
    def __lt__(self, other: Any) -> str:
        return f"{self.value} < {other}"

    def __le__(self, other: Any) -> str:
        return f"{self.value} <= {other}"

    def __gt__(self, other: Any) -> str:
        return f"{self.value} > {other}"

    def __ge__(self, other: Any) -> str:
        return f"{self.value} >= {other}"

    def __eq__(self, other: Any) -> str:  # type: ignore
        value = other
        if isinstance(other, str):
            value = f'"{value}"'
        return f"{self.value} == {value}"

    def __ne__(self, other: Any) -> str:  # type: ignore
        value = other
        if isinstance(other, str):
            value = f'"{value}"'
        return f"{self.value} != {value}"

    # airthmetic operators: add, sub, etc
    def __add__(self, other: Any) -> str:
        return f"{self.value} + {other}"

    def __sub__(self, other: Any) -> str:
        return f"{self.value} - {other}"

    def __mul__(self, other: Any) -> str:
        return f"{self.value} * {other}"

    def __truediv__(self, other: Any) -> str:
        return f"{self.value} / {other}"

    # logical operators: and, or, invert, contains
    def __contains__(self, other: Any) -> str:
        return f"{self.value} IN {other}"

    def __and__(self, other: Any) -> str:
        return f"{self.value} AND {other}"

    def __or__(self, other: Any) -> str:
        return f"{self.value} OR {other}"

    def __invert__(self) -> str:
        return f"NOT {self.value}"

    # unary operators: neg, pos, abs
    def __neg__(self) -> str:
        return f"-{self.value}"

    def __pos__(self) -> str:
        return f"+{self.value}"
