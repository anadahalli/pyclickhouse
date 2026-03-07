import re
from dataclasses import dataclass, field
from typing import Any, Self

from pydantic import BaseModel, create_model

from .engines import Engine
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
    _table_model: type[BaseModel]
    _table_name: str
    _table_config: TableConfig
    _table_columns: dict[str, Column]

    def __init__(
        self,
        model: type[BaseModel],
        name: str,
        config: TableConfig,
        columns: dict[str, Column],
    ) -> None:
        self._table_model = model
        self._table_name = name
        self._table_config = config
        self._table_columns = columns

    def __repr__(self) -> str:
        return f"Table({self._table_name})"

    def __str__(self) -> str:
        return self._table_name

    def __getattr__(self, name: str) -> Expression:
        if name not in self._table_columns:
            raise AttributeError(f"Table({self._table_name}) has no column '{name}'")
        return Expression(self._table_columns[name])

    @classmethod
    def from_model(
        cls,
        model: type[BaseModel],
        *,
        name: str | None = None,
        config: TableConfig | None = None,
    ) -> Self:
        table_name = name or pascal_to_snake(model.__name__)
        table_config = config or TableConfig.from_model(model)
        table_columns = {}
        for name, info in model.model_fields.items():
            table_columns[name] = Column.from_field(name, info)
        table = cls(
            model=model,
            name=table_name,
            config=table_config,
            columns=table_columns,
        )
        return table

    @classmethod
    def from_database(
        cls, name: str, engine: str, columns: list[dict[str, str]]
    ) -> Self:
        table_columns: dict[str, Column] = {
            col["name"]: Column(**col) for col in columns
        }
        table_config = TableConfig.from_database(engine)
        table_model: type[BaseModel] = create_dynamic_model(name, table_columns)
        return cls(
            model=table_model,
            name=name,
            config=table_config,
            columns=table_columns,
        )

    def to_create_sql(self, database: str | None = None) -> str:
        table_name = f"{database}.{self._table_name}" if database else self._table_name
        table_columns = ", ".join(
            [col.to_sql() for col in self._table_columns.values()]
        )
        table_engine = self._table_config.to_sql()
        return f"CREATE TABLE IF NOT EXISTS {table_name} ({table_columns}) {table_engine}".strip()

    def to_drop_sql(self, database: str | None = None) -> str:
        table_name = f"{database}.{self._table_name}" if database else self._table_name
        return f"DROP TABLE IF EXISTS {table_name}"

    def to_insert_sql(self, database: str | None = None) -> str:
        table_name = f"{database}.{self._table_name}" if database else self._table_name
        columns = ", ".join(self._table_columns.keys())
        return f"INSERT INTO {table_name} ({columns}) VALUES".strip()


def create_dynamic_model(name: str, columns: dict[str, Column]) -> type[BaseModel]:
    fields: dict[str, Any] = {}

    for col_name, col in columns.items():
        fields[col_name] = get_python_type(col.type)

    model: type[BaseModel] = create_model(name, **fields)
    return model


def create_result_model(
    columns: list[tuple[str, str]],
    name: str = "Result",
) -> type[BaseModel]:
    fields: dict[str, Any] = {n: get_python_type(t) for n, t in columns}
    return create_model(name, **fields)
