from dataclasses import dataclass
from typing import Any

from .utils import comma_join


class Engine:
    def __init_subclass__(cls, **kwargs: Any) -> None:
        engine_map[cls.__name__] = cls

    def __str__(self) -> str:
        return self.to_sql().strip()

    def to_sql(self) -> str:
        raise NotImplementedError()


engine_map: dict[str, type[Engine]] = {}


@dataclass(kw_only=True)
class Memory(Engine):
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        parts: list[str] = []
        parts.append("Memory")
        if self.settings:
            parts.append(comma_join(self.settings, prefix="SETTINGS"))
        return " ".join(parts)


# MergeTree Family


@dataclass(kw_only=True)
class MergeTree(Engine):
    order_by: str = "tuple()"
    primary_key: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    ttl: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        parts: list[str] = []
        parts.append("MergeTree")
        parts.append(f"ORDER BY {self.order_by}")
        if self.primary_key is not None:
            parts.append(f"PRIMARY KEY {self.primary_key}")
        if self.partition_by is not None:
            parts.append(f"PARTITION BY {self.partition_by}")
        if self.sample_by is not None:
            parts.append(f"SAMPLE BY {self.sample_by}")
        if self.ttl is not None:
            parts.append(f"TTL {self.ttl}")
        if self.settings:
            parts.append(comma_join(self.settings, prefix="SETTINGS"))
        return " ".join(parts)


# @dataclass
# class ReplacingMergeTree(Engine):
#     ver: str | None = None
#     is_deleted: str | None = None
#     order_by: str | None = None
#     primary_key: str | None = None
#     partition_by: str | None = None
#     sample_by: str | None = None
#     settings: dict[str, Any] = field(default_factory=dict)


# class CoalescingMergeTree(Engine):
#     columns: str | None = None
#     order_by: str | None = None
#     partition_by: str | None = None
#     sample_by: str | None = None
#     settings: dict[str, Any] = field(default_factory=dict)


# class SummingMergeTree(Engine):
#     columns: str | None = None
#     order_by: str | None = None
#     partition_by: str | None = None
#     sample_by: str | None = None
#     settings: dict[str, Any] = field(default_factory=dict)


# class AggregatingMergeTree(Engine):
#     ttl: str | None = None
#     order_by: str | None = None
#     partition_by: str | None = None
#     sample_by: str | None = None
#     settings: dict[str, Any] = field(default_factory=dict)


# class CollapsingMergeTree(Engine):
#     sign: str
#     order_by: str | None = None
#     partition_by: str | None = None
#     sample_by: str | None = None
#     settings: dict[str, Any] = field(default_factory=dict)


# class VersionedCollapsingMergeTree(Engine):
#     sign: str
#     version: str
#     order_by: str | None = None
#     partition_by: str | None = None
#     sample_by: str | None = None
#     settings: dict[str, Any] = field(default_factory=dict)


# # integrations


# class Kafka(Engine):
#     kafka_broker_list: str
#     kafka_topic_list: str
#     kafka_group_name: str
#     kafka_format: str
#     settings: dict[str, Any] = field(default_factory=dict)

#     def to_sql(self) -> str:
#         args = [
#             f"'{arg}'" if isinstance(arg, str) else str(arg)
#             for arg in asdict(self).values()
#         ]
#         return f"Kafka({', '.join(args)})"


# class PostgreSQL(Engine):
#     host_port: str
#     database: str
#     table: str
#     user: str
#     password: str
#     schema: str | None = None
