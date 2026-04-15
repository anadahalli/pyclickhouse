from dataclasses import KW_ONLY, dataclass, field, replace
from typing import TYPE_CHECKING, Any, Self

import prqlc

from pyclickhouse.fields import Aggregate, Expression, Function

if TYPE_CHECKING:
    from pyclickhouse.table import Table
    from pyclickhouse.view import View

options = prqlc.CompileOptions(
    target="sql.clickhouse",
    format=False,
    signature_comment=False,
)


@dataclass(frozen=True)
class Query:
    """A query builder for ClickHouse.

    Args:
        table: The table to query.
        database: The database to query from.
        schema: The schema to query from.
        pipeline: The pipeline of steps to execute.
    """

    table: Table | View | str
    _: KW_ONLY
    database: str | None = None
    schema: str | None = None
    pipeline: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.pipeline:
            step = f"from {self._table_name()}"
            self.pipeline.append(step)

    def build(self) -> str:
        """Build the full PRQL query

        Returns:
            The full PRQL query.
        """
        return " | ".join(self.pipeline)

    def compile(self) -> str:
        """Compile the PRQL query to SQL

        Returns:
            The compiled SQL query.
        """
        return prqlc.compile(self.build(), options=options)

    def __repr__(self) -> str:
        return self.build()

    def __str__(self) -> str:
        return self.compile()

    def _table_name(self) -> str:
        return ".".join(filter(None, [self.schema, self.database, str(self.table)]))

    def _stringify(self, value: Any) -> str:
        if isinstance(value, Aggregate):
            return str(value)
        if isinstance(value, Expression):
            return str(value)
        if isinstance(value, Function):
            return value.to_sql()
        return value

    def _from_args(self, *args: Any) -> list[str]:
        return [self._stringify(col) for col in args]

    def _from_kwargs(self, **kwargs: Any) -> list[str]:
        return [f"{key} = {self._stringify(val)}" for key, val in kwargs.items()]

    def _copy(self, step: str) -> Self:
        return replace(self, pipeline=[*self.pipeline, step])

    def _join(self, items: list[str]) -> str:
        return ", ".join(items)

    def select(self, *args: Any, **kwargs: Any) -> Self:
        """Select columns from the table.

        Args:
            *args: Column names to select.
            **kwargs: Column name-value pairs to select.

        Returns:
            A new `Query` with the select step added.
        """
        if items := [*self._from_args(*args), *self._from_kwargs(**kwargs)]:
            step = f"select {{{self._join(items)}}}"
            return self._copy(step)
        raise ValueError("select requires at least one argument")

    def derive(self, **kwargs: Any) -> Self:
        """Derive new columns from existing ones.

        Args:
            **kwargs: Column name-expression pairs to derive.

        Returns:
            A new `Query` with the derive step added.
        """
        if items := [*self._from_kwargs(**kwargs)]:
            step = f"derive {{{self._join(items)}}}"
            return self._copy(step)
        raise ValueError("derive requires at least one argument")

    def sort(self, *args: Any) -> Self:
        """Sort the table by the given columns.

        Args:
            *args: Column names to sort by.

        Returns:
            A new `Query` with the sort step added.
        """
        if items := [*self._from_args(*args)]:
            step = f"sort {{{self._join(items)}}}"
            return self._copy(step)
        raise ValueError("sort requires at least one argument")

    def filter(self, expression: Any) -> Self:
        """Filter the table by the given expression.

        Args:
            expression: The expression to filter by.

        Returns:
            A new `Query` with the filter step added.
        """
        step = f"filter ({str(expression)})"
        return self._copy(step)

    def aggregate(self, *args: Any, **kwargs: Any) -> Self:
        """Aggregate the table by the given columns.

        Args:
            *args: Column names to aggregate by.
            **kwargs: Aggregate name-expression pairs.

        Returns:
            A new `Query` with the aggregate step added.
        """
        if items := [*self._from_args(*args), *self._from_kwargs(**kwargs)]:
            step = f"aggregate {{{self._join(items)}}}"
            return self._copy(step)
        raise ValueError("aggregate requires at least one argument")

    def group(self, *args: Any, **kwargs: Any) -> Self:
        """Group the table by the given columns and aggregate.

        Args:
            *args: Column names to group by.
            **kwargs: Aggregate name-expression pairs.

        Returns:
            A new `Query` with the group step added.
        """
        groups: list[str] = []
        aggregates: list[str] = []

        for col in args:
            if isinstance(col, Aggregate):
                aggregates.append(self._stringify(col))
            else:
                groups.append(self._stringify(col))
        for name, col in kwargs.items():
            if isinstance(col, Aggregate):
                aggregates.append(f"{name} = {self._stringify(col)}")
            else:
                groups.append(f"{name} = {self._stringify(col)}")

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
        """Take a subset of the table by row index.

        Args:
            n: Number of rows to take.
            start: Starting row index (inclusive).
            end: Ending row index (exclusive).

        Returns:
            A new `Query` with the take step added.
        """
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
