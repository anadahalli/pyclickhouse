from dataclasses import dataclass
from typing import ClassVar


class Engine:
    name: ClassVar

    def to_sql(self) -> str:
        raise NotImplementedError()


@dataclass(kw_only=True)
class Memory(Engine):
    name: ClassVar = "Memory"

    def to_sql(self) -> str:
        return self.name


@dataclass(kw_only=True)
class MergeTree(Engine):
    name: ClassVar = "MergeTree()"

    order_by: str | None = None
    partition_by: str | None = None
    primary_key: str | None = None

    def to_sql(self) -> str:
        parts: list[str] = []

        if self.order_by is not None:
            parts.append(f"ORDER BY {self.order_by}")
        else:
            parts.append("ORDER BY tuple()")

        if self.partition_by is not None:
            parts.append(f"PARTITION BY {self.partition_by}")

        if self.primary_key is not None:
            parts.append(f"PRIMARY KEY {self.primary_key}")

        return f"{self.name} {' '.join(parts)}".strip()
