from dataclasses import dataclass
from typing import Any

from .utils import comma_join


class Engine:
    """Base class for ClickHouse engines."""

    def __init_subclass__(cls, **kwargs: Any) -> None:
        engine_map[cls.__name__] = cls

    def __str__(self) -> str:
        return self.to_sql().strip()

    def to_sql(self) -> str:
        """Returns the SQL representation of the engine."""
        raise NotImplementedError()


engine_map: dict[str, type[Engine]] = {}


@dataclass(kw_only=True)
class Memory(Engine):
    """
    Memory engine.

    Args:
        settings: dictionary of engine settings.
    """

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
    """
    MergeTree engine.

    Args:
        order_by: by expression.
        primary_key: primary key expression.
        partition_by: partition by expression.
        sample_by: sample by expression.
        ttl: TTL expression.
        settings: dictionary of engine settings.
    """

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


@dataclass(kw_only=True)
class ReplacingMergeTree(Engine):
    """
    ReplacingMergeTree engine.

    Args:
        ver: version column.
        is_deleted: deleted column.
        order_by: order by expression.
        primary_key: primary key expression.
        partition_by: partition by expression.
        sample_by: sample by expression.
        settings: dictionary of engine settings.
    """

    ver: str | None = None
    is_deleted: str | None = None
    order_by: str | None = None
    primary_key: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        args: list[str] = []
        if self.ver is not None:
            args.append(self.ver)
        if self.is_deleted is not None:
            args.append(self.is_deleted)
        parts: list[str] = []
        parts.append(f"ReplacingMergeTree({', '.join(args)})")
        parts.append(f"ORDER BY {self.order_by}")
        if self.primary_key is not None:
            parts.append(f"PRIMARY KEY {self.primary_key}")
        if self.partition_by is not None:
            parts.append(f"PARTITION BY {self.partition_by}")
        if self.sample_by is not None:
            parts.append(f"SAMPLE BY {self.sample_by}")
        if self.settings:
            parts.append(comma_join(self.settings, prefix="SETTINGS"))
        return " ".join(parts)


@dataclass(kw_only=True)
class CoalescingMergeTree(Engine):
    """CoalescingMergeTree engine.

    Args:
        columns: columns expression.
        order_by: order by expression.
        partition_by: partition by expression.
        sample_by: sample by expression.
        settings: dictionary of engine settings.
    """

    columns: str | None = None
    order_by: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        raise NotImplementedError()


@dataclass(kw_only=True)
class SummingMergeTree(Engine):
    """SummingMergeTree engine.

    Args:
        columns: columns expression.
        order_by: order by expression.
        partition_by: partition by expression.
        sample_by: sample by expression.
        settings: dictionary of engine settings.
    """

    columns: str | None = None
    order_by: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None


@dataclass(kw_only=True)
class AggregatingMergeTree(Engine):
    """AggregatingMergeTree engine.

    Args:
        columns: columns expression.
        order_by: order by expression.
        partition_by: partition by expression.
        sample_by: sample by expression.
        settings: dictionary of engine settings.
    """

    columns: str | None = None
    order_by: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        raise NotImplementedError()


@dataclass(kw_only=True)
class CollapsingMergeTree(Engine):
    """CollapsingMergeTree engine.

    Args:
        sign: sign column expression.
        order_by: order by expression.
        partition_by: partition by expression.
        sample_by: sample by expression.
        settings: dictionary of engine settings.
    """

    sign: str
    order_by: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        raise NotImplementedError()


@dataclass(kw_only=True)
class VersionedCollapsingMergeTree(Engine):
    """VersionedCollapsingMergeTree engine.

    Args:
        sign: sign column expression.
        version: version column expression.
        order_by: order by expression.
        partition_by: partition by expression.
        sample_by: sample by expression.
        settings: dictionary of engine settings.
    """

    sign: str
    version: str
    order_by: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        raise NotImplementedError()


# integrations


@dataclass(kw_only=True)
class Kafka(Engine):
    """Kafka engine.

    Args:
        broker_list: broker list.
        topic_list: topic list.
        group_name: group name.
        format: format.
        settings: dictionary of engine settings.
    """

    broker_list: str
    topic_list: str
    group_name: str
    format: str
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        parts: list[str] = []
        parts.append(
            f"Kafka('{self.broker_list}', '{self.topic_list}', '{self.group_name}', '{self.format}'"
        )
        if self.settings:
            parts.append(comma_join(self.settings, prefix="SETTINGS"))
        return " ".join(parts)


@dataclass(kw_only=True)
class PostgreSQL(Engine):
    """PostgreSQL engine.

    Args:
        host_port: host and port.
        database: database name.
        table: table name.
        user: user name.
        password: password.
        schema: schema name.
    """

    host_port: str
    database: str
    table: str
    user: str
    password: str
    schema: str | None = None

    def to_sql(self) -> str:
        raise NotImplementedError()
