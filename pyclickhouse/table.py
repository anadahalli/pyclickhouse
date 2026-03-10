from typing import Any, Self

from pydantic import BaseModel, create_model

from .engines import Engine, MergeTree
from .fields import Column, Expression
from .registry import Registry, registry
from .types import Lifecycle, get_python_type
from .utils import pascal_to_snake


class Table:
    """
    Create a new table from a Pydantic model.

    Args:
        model: The Pydantic model to create the table from.
        name: The name of the table. Defaults to the snake_case version of the model name.
        engine: The engine to use for the table. Defaults to MergeTree().
        columns: The columns to use for the table. Defaults to the columns defined in the model.
        comment: The comment to use for the table. Defaults to None.
        lifecycle: The lifecycle to use for the table. Defaults to Lifecycle.managed.
    """

    def __init__(
        self,
        model: type[BaseModel],
        *,
        name: str | None = None,
        engine: Engine | str | None = None,
        columns: dict[str, Column] | None = None,
        comment: str | None = None,
        lifecycle: Lifecycle = Lifecycle.managed,
        registry: Registry = registry,
    ) -> None:
        self._model = model
        self._name: str = name or pascal_to_snake(model.__name__)
        self._engine: Engine | str = engine or MergeTree()
        self._columns: dict[str, Column] = columns or {
            name: Column.from_field(name, info)
            for name, info in model.model_fields.items()
        }
        self._comment = comment
        self._lifecycle = lifecycle
        self._registry = registry
        registry.register_table(self)

    def __repr__(self) -> str:
        return f"Table({self._name})"

    def __str__(self) -> str:
        return self._name

    def __getattr__(self, name: str) -> Expression:
        if name not in self._columns:
            raise AttributeError(f"Table({self._name}) has no column '{name}'")
        return Expression(self._columns[name])

    def get_model(self) -> type[BaseModel]:
        return self._model

    def get_name(self) -> str:
        return self._name

    def get_engine(self) -> str:
        return str(self._engine)

    def get_columns(self) -> dict[str, Column]:
        return self._columns

    def get_lifecycle(self) -> Lifecycle:
        return self._lifecycle

    @classmethod
    def from_sql(
        cls,
        name: str,
        columns: list[dict[str, str]],
        engine: str,
    ) -> Self:
        """
        Create a new table from a SQL table definition.

        Args:
            name: The name of the table.
            columns: The columns of the table.
            engine: The engine to use for the table.

        Returns:
            A new Table instance.
        """
        table_columns: dict[str, Column] = {
            col["name"]: Column(**col) for col in columns
        }
        fields: dict[str, Any] = {}
        for col_name, col in table_columns.items():
            fields[col_name] = get_python_type(str(col.type))
        model: type[BaseModel] = create_model(name, **fields)
        return cls(
            model=model,
            name=name,
            engine=engine,
            columns=table_columns,
        )
