from dataclasses import KW_ONLY, dataclass, field, replace
from typing import Any, Self

import prqlc

from .fields import Aggregate, Expression
from .table import Table

options = prqlc.CompileOptions(
    target="sql.clickhouse",
    format=False,
    signature_comment=False,
)


@dataclass(frozen=True)
class Query:
    table: Table | str
    _: KW_ONLY
    database: str | None = None
    schema: str | None = None
    pipeline: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.pipeline:
            step = f"from {self._table_name()}"
            self.pipeline.append(step)

    def build(self) -> str:
        return " | ".join(self.pipeline)

    def compile(self) -> str:
        return prqlc.compile(self.build(), options=options)

    def __repr__(self) -> str:
        return self.build()

    def __str__(self) -> str:
        return self.compile()

    def _table_name(self) -> str:
        names = [self.schema, self.database, str(self.table)]
        return ".".join(filter(None, names))

    def _from_args(self, *args: Any) -> list[str]:
        return [str(col) for col in args]

    def _from_kwargs(self, **kwargs: Any) -> list[str]:
        return [f"{key} = {str(val)}" for key, val in kwargs.items()]

    def _copy(self, step: str) -> Self:
        return replace(self, pipeline=[*self.pipeline, step])

    def _join(self, items: list[str]) -> str:
        return ", ".join(items)

    def select(self, *args: Any, **kwargs: Any) -> Self:
        if items := [*self._from_args(*args), *self._from_kwargs(**kwargs)]:
            step = f"select {{{self._join(items)}}}"
            return self._copy(step)
        raise ValueError("select requires at least one argument")

    def derive(self, **kwargs: Any) -> Self:
        if items := [*self._from_kwargs(**kwargs)]:
            step = f"derive {{{self._join(items)}}}"
            return self._copy(step)
        raise ValueError("derive requires at least one argument")

    def sort(self, *args: Any) -> Self:
        if items := [*self._from_args(*args)]:
            step = f"sort {{{self._join(items)}}}"
            return self._copy(step)
        raise ValueError("sort requires at least one argument")

    def filter(self, expression: Any) -> Self:
        step = f"filter ({str(expression)})"
        return self._copy(step)

    def aggregate(self, *args: Any, **kwargs: Any) -> Self:
        if items := [*self._from_args(*args), *self._from_kwargs(**kwargs)]:
            step = f"aggregate {{{self._join(items)}}}"
            return self._copy(step)
        raise ValueError("aggregate requires at least one argument")

    def group(self, *args: Any, **kwargs: Any) -> Self:
        groups: list[str] = []
        aggregates: list[str] = []

        for col in args:
            if isinstance(col, Aggregate):
                aggregates.append(str(col))
            elif isinstance(col, Expression):
                groups.append(str(col))
        for name, col in kwargs.items():
            if isinstance(col, Aggregate):
                aggregates.append(f"{name} = {str(col)}")
            elif isinstance(col, Expression):
                groups.append(f"{name} = {str(col)}")

        group = f"group {{{self._join(groups)}}}"
        aggregate = f"aggregate {{{self._join(aggregates)}}}"
        step = f"{group} ({aggregate})"
        return self._copy(step)

    def take(
        self,
        n: int | None = None,
        *,
        start: int | None = None,
        end: int | None = None,
    ) -> Self:
        if n is None:
            if start is None and end is None:
                raise ValueError("either n or (start or end) must be specified")
            elif start is not None and end is None:
                range = f"{start}.."
            elif start is None and end is not None:
                range = f"..{end}"
            else:
                range = f"{start}..{end}"
        else:
            if start is not None or end is not None:
                raise ValueError("both n and (start or end) can not be specified")
            range = f"{n}"

        step = f"take {range}"
        return self._copy(step)

    def window(
        self,
        rows: Any,
        range: Any,
        expanding: bool | None = None,
        rolling: int | None = None,
        *,
        pipeline: Any | None = None,
    ) -> Self:
        raise NotImplementedError()

    def join(self) -> Self:
        raise NotImplementedError()

    def exclude(self) -> Self:
        raise NotImplementedError()
