import re
from dataclasses import dataclass, field
from typing import Any, Self

from pydantic import BaseModel, create_model

from .engines import Engine, MergeTree
from .fields import Column, Expression
from .types import get_python_type
from .utils import pascal_to_snake


@dataclass
class TableConfig:
    engine: Engine | str = field(default="MergeTree")
    order_by: str | None = field(default=None)
    settings: dict[str, Any] = field(default_factory=dict)

    def to_sql(self) -> str:
        engine = self.engine
        if isinstance(self.engine, Engine):
            engine = self.engine.to_sql()
        order_by = self.order_by or "tuple()"
        settings = ", ".join([f"{k} = {v}" for k, v in self.settings.items()])
        return f"ENGINE = {engine} ORDER BY {order_by} {settings}".strip()

    @classmethod
    def from_model(cls, model: type[BaseModel]) -> Self:
        class_vars = [getattr(model, name) for name in model.__class_vars__]
        configs = [config for config in class_vars if isinstance(config, TableConfig)]
        table_config = configs[0] if configs else cls()
        return table_config

    @classmethod
    def from_database(cls, engine_full: str) -> Self:
        pattern = r"(?P<engine>\w+)\s+ORDER BY\s+(?P<order_by>.+?)\s+SETTINGS\s+(?P<settings>.*)"
        match = re.search(pattern, engine_full)

        if not match:
            raise ValueError("Could not parse engine string")

        engine = match.group("engine")
        order_by = match.group("order_by")
        settings_raw = match.group("settings")

        settings = {}
        for item in settings_raw.split(","):
            k, v = item.split("=")
            settings[k.strip()] = v.strip().strip("'\"")

        return cls(engine=engine, order_by=order_by, settings=settings)


class Table:
    _model: type[BaseModel]
    _name: str
    _engine: Engine | str
    _columns: dict[str, Column]
    _comment: str | None

    def __init__(
        self,
        model: type[BaseModel],
        name: str,
        engine: Engine | str,
        columns: dict[str, Column],
        comment: str | None = None,
    ) -> None:
        self._model = model
        self._name = name
        self._engine = engine
        self._columns = columns
        self._comment = comment

    def __repr__(self) -> str:
        return f"Table({self._name})"

    def __str__(self) -> str:
        return self._name

    def __getattr__(self, name: str) -> Expression:
        if name not in self._columns:
            raise AttributeError(f"Table({self._name}) has no column '{name}'")
        return Expression(self._columns[name])

    @classmethod
    def from_model(
        cls,
        model: type[BaseModel],
        *,
        name: str | None = None,
        engine: Engine | str | None = None,
        comment: str | None = None,
    ) -> Self:
        name = name or pascal_to_snake(model.__name__)
        engine = engine or MergeTree()
        columns = {
            name: Column.from_field(name, info)
            for name, info in model.model_fields.items()
        }
        table = cls(
            model=model,
            name=name,
            engine=engine,
            columns=columns,
        )
        return table

    @classmethod
    def from_sql(
        cls,
        name: str,
        engine_sql: str,
        columns_sql: list[dict[str, str]],
    ) -> Self:
        columns = {col["name"]: Column(**col) for col in columns_sql}
        model = create_dynamic_model(name, columns)
        return cls(
            model=model,
            name=name,
            engine=engine_sql,
            columns=columns,
        )

    def to_create_sql(self, database: str | None = None) -> str:
        table_name = f"{database}.{self._name}" if database else self._name
        table_columns = ", ".join([col.to_sql() for col in self._columns.values()])
        table_engine = str(self._engine)
        return f"{table_name} ({table_columns}) ENGINE = {table_engine}".strip()

    def to_insert_sql(self, database: str | None = None) -> str:
        table_name = f"{database}.{self._name}" if database else self._name
        columns = ", ".join(self._columns.keys())
        return f"{table_name} ({columns}) VALUES".strip()


def table(
    model: type[BaseModel],
    *,
    name: str | None = None,
    engine: Engine | str | None = None,
    comment: str | None = None,
) -> Table:
    return Table.from_model(model, name=name, engine=engine, comment=comment)


def create_dynamic_model(name: str, columns: dict[str, Column]) -> type[BaseModel]:
    fields: dict[str, Any] = {}
    for col_name, col in columns.items():
        fields[col_name] = get_python_type(str(col.type))
    model: type[BaseModel] = create_model(name, **fields)
    return model


def create_result_model(
    columns: list[tuple[str, str]],
    name: str = "Result",
) -> type[BaseModel]:
    fields: dict[str, Any] = {n: get_python_type(t) for n, t in columns}
    return create_model(name, **fields)
