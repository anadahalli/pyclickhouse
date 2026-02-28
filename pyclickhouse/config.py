from dataclasses import KW_ONLY, dataclass, field
from typing import Self

from pydantic import BaseModel

from .engine import Engine, MergeTree
from .registry import Registry, default_registry
from .utils import pascal_to_snake


@dataclass
class TableConfig:
    engine: Engine = field(default_factory=MergeTree)

    _: KW_ONLY

    name: str | None = None
    comment: str | None = None
    ttl: str | None = None

    settings: dict[str, str] = field(default_factory=dict)
    constraints: dict[str, str] = field(default_factory=dict)
    indexes: dict[str, str] = field(default_factory=dict)
    projections: dict[str, str] = field(default_factory=dict)

    registry: Registry = field(default=default_registry)

    @classmethod
    def from_model(cls, model: type[BaseModel]) -> Self:
        table_engine: Engine = getattr(model, "table_engine", MergeTree())
        table_name: str = pascal_to_snake(model.__name__)

        config: TableConfig = getattr(model, "table_config", cls(engine=table_engine))

        if config.name is None:
            config.name = table_name

        return config
