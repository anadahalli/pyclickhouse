from typing import TYPE_CHECKING, Any, ClassVar, Self

from pydantic import BaseModel
from pydantic._internal._model_construction import ModelMetaclass

from .column import Column
from .config import TableConfig
from .expression import Expression
from .utils import pascal_to_snake


class TableMeta(ModelMetaclass):
    if not TYPE_CHECKING:

        def __getattr__(self, item: str) -> Any:
            """This is necessary to keep attribute access working for class attribute access."""
            table_columns = self.__dict__.get("table_columns")
            if table_columns and item in table_columns:
                return Expression(table_columns[item])

            private_attributes = self.__dict__.get("__private_attributes__")
            if private_attributes and item in private_attributes:
                return private_attributes[item]

            raise AttributeError(item)


class Table(BaseModel, metaclass=TableMeta):
    table_config: ClassVar[TableConfig] = TableConfig()
    table_columns: ClassVar[dict[str, Column]] = {}

    @classmethod
    def __pydantic_init_subclass__(cls: type[Self], **kwargs: Any) -> None:
        cls.model_config["from_attributes"] = True

        if cls.table_config.name is None:
            cls.table_config.name = pascal_to_snake(cls.__name__)

        cls.table_columns = {
            name: Column.from_field(name, field)
            for name, field in cls.model_fields.items()
        }

    @classmethod
    def model_columns(cls) -> dict[str, Column]:
        return cls.table_columns

    @classmethod
    def get_table_name(cls) -> str:
        return cls.table_config.name or ""

    @classmethod
    def to_create_sql(cls) -> str:
        config = cls.table_config
        columns = cls.table_columns

        create = f"CREATE TABLE IF NOT EXISTS {config.name}"
        engine = config.engine.to_sql()
        columns: list[str] = [col.to_sql() for col in columns.values()]
        options: list[str] = []

        if config.comment is not None:
            options.append(f"COMMENT '{config.comment}'")

        if config.ttl is not None:
            options.append(f"TTL {config.ttl}")

        return f"{create} ({', '.join(columns)}) {engine} {' '.join(options)}".strip()

    def to_insert_sql(self) -> str:
        columns: list[str] = [
            col.name for col in self.table_columns.values() if col.name is not None
        ]

        return f"INSERT INTO {self.table_config.name} ({', '.join(columns)}) VALUES"
