from typing import Any, Self

import prqlc
from pydantic import BaseModel, create_model

from .column import Column
from .expression import Expression
from .table import Table
from .types import get_python_type


class Query:
    def __init__(self, table: type[Table]) -> None:
        self._table = table
        self._pipeline: list[str] = [f"from {table.get_table_name()}"]
        self._options = prqlc.CompileOptions(
            target="sql.clickhouse",
            format=False,
            signature_comment=False,
        )

    def _step(self, str) -> None:
        self._pipeline.append(str)

    def _build(self) -> str:
        return " | ".join(self._pipeline)

    def _compile(self) -> str:
        return prqlc.compile(self._build(), self._options)

    def __str__(self) -> str:
        return self._compile()

    def select(self, *args: Any, **kwargs: Any) -> Self:
        names: list[str] = [str(col) for col in args]
        aliases: list[str] = [f"{str(key)} = {str(val)}" for key, val in kwargs.items()]
        if names or aliases:
            items: str = ", ".join([*names, *aliases])
            self._step(f"select {{{items}}}")
        return self

    def derive(self, **kwargs: Any) -> Self:
        columns: list[str] = [f"{key} = {str(val)}" for key, val in kwargs.items()]
        if columns:
            self._step(f"derive {{{', '.join(columns)}}}")
        return self

    def filter(self, expression: Any) -> Self:
        self._step(f"filter ({str(expression)})")
        return self

    def sort(self, *args: Any) -> Self:
        columns: list[str] = [str(col) for col in args]
        if columns:
            self._step(f"sort {{{', '.join(columns)}}}")
        return self

    def take(
        self,
        limit: int | None = None,
        *,
        start: int | None = None,
        end: int | None = None,
    ) -> Self:
        if limit is None and start is None and end is None:
            raise ValueError("either limit or (start or end) must be specified")

        if limit is not None and (start is not None or end is not None):
            raise ValueError("both limit and (start or end) can not be specified")

        if limit is not None:
            range = f"{limit}"
        elif start is None and end is not None:
            range = f"..{end}"
        if start is not None and end is None:
            range = f"{start}.."
        elif start is not None and end is not None:
            range = f"{start}..{end}"
        self._step(f"take {range}")
        return self

    def aggregate(self, *args: Any, **kwargs: Any) -> Self:
        names: list[str] = [str(col) for col in args]
        aliases: list[str] = [f"{str(key)} = {str(val)}" for key, val in kwargs.items()]
        if names or aliases:
            items: str = ", ".join([*names, *aliases])
            self._step(f"aggregate {{{items}}}")
        return self

    def group(self, *args: Any, **kwargs: Any) -> Self:
        groups: list[str] = []
        aggregates: list[str] = []

        for col in args:
            if isinstance(col, Expression):
                if isinstance(col._value, Column):
                    groups.append(str(col))
                elif isinstance(col._value, str):
                    aggregates.append(str(col))
        for name, col in kwargs.items():
            if isinstance(col, Expression):
                if isinstance(col._value, Column):
                    groups.append(f"{name} = {str(col)}")
                elif isinstance(col._value, str):
                    aggregates.append(f"{name} = {str(col)}")

        group = f"group {{{', '.join(groups)}}}"
        aggregate = f"(aggregate {{{', '.join(aggregates)}}})"
        self._step(f"{group} {aggregate}")
        return self

    def window(
        self,
        rows: Any,
        range: Any,
        expanding: bool | None = None,
        rolling: int | None = None,
        *,
        pipeline: Any | None = None,
    ) -> Self:
        return self

    def join(self) -> Self:
        return self


class Result(BaseModel):
    pass


def create_result_model(name: str, columns: Any) -> type[BaseModel]:
    fields: dict[str, Any] = {}

    for col_name, col_type in columns:
        fields[col_name] = get_python_type(col_type)

    model: type[BaseModel] = create_model(name, **fields)
    return model
