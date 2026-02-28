from dataclasses import KW_ONLY, dataclass, field
from typing import Self

from pydantic import BaseModel

from .engine import Engine, MergeTree


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

    @classmethod
    def from_model(cls, model: type[BaseModel]) -> Self:
        class_vars = vars(model).values()

        config: TableConfig = next(
            (cnf for cnf in class_vars if isinstance(cnf, TableConfig)), cls()
        )

        if config.engine is None:
            config.engine = MergeTree()

        if config.name is None:
            config.name = model.__name__.lower()

        return config
