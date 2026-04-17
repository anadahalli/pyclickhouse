import logging
from dataclasses import dataclass
from typing import Any

from pyclickhouse.utils import comma_join

logger = logging.getLogger(__name__)

engine_map: dict[str, type["Engine"]] = {}


def _build_merge_tree_sql(
    name: str,
    *,
    args: list[str] | None = None,
    order_by: str | None = None,
    primary_key: str | None = None,
    partition_by: str | None = None,
    sample_by: str | None = None,
    ttl: str | None = None,
    settings: dict[str, Any] | None = None,
) -> str:
    parts = [f"{name}({', '.join(args)})" if args else name]
    if order_by:
        parts.append(f"ORDER BY {order_by}")
    if primary_key:
        parts.append(f"PRIMARY KEY {primary_key}")
    if partition_by:
        parts.append(f"PARTITION BY {partition_by}")
    if sample_by:
        parts.append(f"SAMPLE BY {sample_by}")
    if ttl:
        parts.append(f"TTL {ttl}")
    if settings:
        parts.append(comma_join(settings, prefix="SETTINGS"))
    return " ".join(parts)


def _base_sql(
    name: str,
    *,
    args: list[str] | None = None,
    settings: dict[str, Any] | None = None,
) -> str:
    parts = [f"{name}({', '.join(args)})" if args else name]
    if settings:
        parts.append(comma_join(settings, prefix="SETTINGS"))
    return " ".join(parts)


class Engine:
    """Base class for ClickHouse table engines.

    All engine classes inherit from this base class. Engines are registered
    automatically in `engine_map` when subclasses are defined.

    Attributes:
        name: The engine class name.
        full_engine: The full SQL engine expression.

    Examples:
        >>> from pyclickhouse.engines import MergeTree, build_engine
        >>> engine = MergeTree(order_by="id")
        >>> print(engine)
        MergeTree ORDER BY id
        >>> parsed = build_engine("MergeTree ORDER BY id")
        >>> print(parsed.full_engine)
        MergeTree ORDER BY id
    """

    name: str = ""
    full_engine: str = ""

    def __init_subclass__(cls, **kwargs: Any) -> None:
        engine_map[cls.__name__] = cls

    def __post_init__(self) -> None:
        if not self.full_engine:
            self.full_engine = self.to_sql()

    def to_sql(self) -> str:
        """Create the full SQL engine expression from the engine name and arguments.

        Returns:
            The full SQL engine expression.
        """
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.full_engine.strip()

    @classmethod
    def from_sql(cls, full_engine: str) -> "Engine | None":
        """Create an Engine instance from a ClickHouse full_engine SQL expression.

        Args:
            full_engine: The full engine SQL string (e.g., "MergeTree ORDER BY id").

        Returns:
            An Engine instance with name and full_engine set, or None if the
            engine type is unknown.

        Examples:
            >>> engine = Engine.from_sql("MergeTree ORDER BY id")
            >>> engine.name
            'MergeTree'
        """
        if not full_engine:
            return None
        name = full_engine.split(" ")[0].split("(")[0]
        try:
            engine_cls = engine_map[name]
        except KeyError:
            if not name.startswith("System"):
                logger.warning("Engine %s not found", name)
            return None
        engine = engine_cls.__new__(engine_cls)
        engine.name = name
        engine.full_engine = full_engine
        return engine


# Simple engines


@dataclass(kw_only=True)
class Memory(Engine):
    """[`Memory`](https://clickhouse.com/docs/en/engines/table-engines/special/memory) engine that stores data in RAM.

    Data is stored in RAM and is not persisted. Useful for testing or
    temporary data that doesn't need persistence.

    Args:
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = Memory()
        >>> print(engine)
        Memory
    """

    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        return _base_sql("Memory", settings=self.settings)


@dataclass(kw_only=True)
class Null(Engine):
    """[`Null`](https://clickhouse.com/docs/en/engines/table-engines/special/null) engine that writes data but immediately discards it.

    All data is written but never stored. Useful for testing write
    performance or discarding unwanted data.

    Examples:
        >>> engine = Null()
        >>> print(engine)
        Null
    """

    def to_sql(self) -> str:
        return "Null"


@dataclass(kw_only=True)
class Log(Engine):
    """[`Log`](https://clickhouse.com/docs/en/engines/table-engines/log-family/log) engine with basic table logging functionality.

    Stores data in a log file with basic support for concurrent access.
    Suitable for small to medium tables with frequent inserts.

    Args:
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = Log()
        >>> print(engine)
        Log
    """

    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        return _base_sql("Log", settings=self.settings)


@dataclass(kw_only=True)
class StripeLog(Engine):
    """[`StripeLog`](https://clickhouse.com/docs/en/engines/table-engines/log-family/stripelog) engine optimized for sequential writes.

    Stores data in stripes, optimized for bulk insert operations.
    Better write performance than Log for sequential writes.

    Args:
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = StripeLog()
        >>> print(engine)
        StripeLog
    """

    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        return _base_sql("StripeLog", settings=self.settings)


@dataclass(kw_only=True)
class TinyLog(Engine):
    """[`TinyLog`](https://clickhouse.com/docs/en/engines/table-engines/log-family/tinylog) engine with minimal storage overhead.

    Lightweight logging engine with minimal metadata storage.
    Good for tables with many small columns.

    Args:
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = TinyLog()
        >>> print(engine)
        TinyLog
    """

    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        return _base_sql("TinyLog", settings=self.settings)


@dataclass(kw_only=True)
class Set(Engine):
    """[`Set`](https://clickhouse.com/docs/en/engines/table-engines/special/set) engine for storing unique values.

    Stores a set of unique values that can be used for IN queries
    and set operations.

    Args:
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = Set()
        >>> print(engine)
        Set
    """

    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        return _base_sql("Set", settings=self.settings)


@dataclass(kw_only=True)
class Dictionary(Engine):
    """[`Dictionary`](https://clickhouse.com/docs/en/engines/table-engines/special/dictionary) engine for accessing external dictionaries.

    Provides access to data from external dictionaries configured
    in ClickHouse.

    Args:
        dictionary: The name of the dictionary to use.

    Examples:
        >>> engine = Dictionary(dictionary="my_dict")
        >>> print(engine)
        Dictionary('my_dict')
    """

    dictionary: str

    def to_sql(self) -> str:
        return _base_sql("Dictionary", args=[f"'{self.dictionary}'"])


@dataclass(kw_only=True)
class Merge(Engine):
    """[`Merge`](https://clickhouse.com/docs/en/engines/table-engines/special/merge) engine for reading from multiple tables.

    Allows reading from multiple tables matching a regular expression.
    The actual tables must be on the same server.

    Args:
        db_name: The database name or a regex pattern.
        tables_regexp: Regular expression to match table names.

    Examples:
        >>> engine = Merge(db_name="mydb", tables_regexp=".*")
        >>> print(engine)
        Merge(mydb, '.*')
    """

    db_name: str
    tables_regexp: str

    def to_sql(self) -> str:
        return _base_sql("Merge", args=[self.db_name, f"'{self.tables_regexp}'"])


@dataclass(kw_only=True)
class File(Engine):
    """[`File`](https://clickhouse.com/docs/en/engines/table-engines/special/file) engine for reading/writing files.

    Allows reading and writing files in various formats directly.

    Args:
        fmt: The file format (e.g., 'CSV', 'JSON', 'Parquet').

    Examples:
        >>> engine = File(fmt="CSV")
        >>> print(engine)
        File('CSV')
    """

    fmt: str

    def to_sql(self) -> str:
        return _base_sql("File", args=[f"'{self.fmt}'"])


@dataclass(kw_only=True)
class Distributed(Engine):
    """[`Distributed`](https://clickhouse.com/docs/en/engines/table-engines/special/distributed) engine for querying remote servers.

    Provides a way to query data across multiple remote servers.
    The table itself doesn't store data, just coordinates queries.

    Args:
        cluster: The cluster name in the ClickHouse configuration.
        database: The database name on remote servers.
        table: The table name on remote servers.
        sharding_key: Optional sharding key for write operations.
        policy_name: Optional storage policy name.
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = Distributed(cluster="mycluster", database="mydb", table="mytable")
        >>> print(engine)
        Distributed(mycluster, mydb, mytable)
    """

    cluster: str
    database: str
    table: str
    sharding_key: str | None = None
    policy_name: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        args = [self.cluster, self.database, self.table]
        if self.sharding_key:
            args.append(self.sharding_key)
        if self.policy_name:
            args.append(self.policy_name)
        return _base_sql("Distributed", args=args, settings=self.settings)


# MergeTree Family


@dataclass(kw_only=True)
class MergeTree(Engine):
    """[`MergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree) main engine for storing and merging data.

    The most commonly used engine for large tables. Supports:
    - Custom sorting keys via ORDER BY
    - Partitioning via PARTITION BY
    - Data sampling via SAMPLE BY
    - TTL for automatic data expiration

    Args:
        order_by: Sorting key expression. Defaults to 'tuple()'.
        primary_key: Primary key expression (can differ from order_by).
        partition_by: Partition key expression for organizing data.
        sample_by: Sampling expression for approximate queries.
        ttl: TTL expression for automatic data expiration.
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = MergeTree(order_by="id", partition_by="toYYYYMM(date)")
        >>> print(engine)
        MergeTree ORDER BY id PARTITION BY toYYYYMM(date)
    """

    order_by: str = "tuple()"
    primary_key: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    ttl: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        return _build_merge_tree_sql(
            "MergeTree",
            order_by=self.order_by,
            primary_key=self.primary_key,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            ttl=self.ttl,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class SharedMergeTree(MergeTree):
    """[`SharedMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/sharedmergetree) engine with shared metadata.

    Similar to MergeTree but shares metadata across replicas.

    Examples:
        >>> engine = SharedMergeTree(order_by="id")
        >>> print(engine)
        SharedMergeTree ORDER BY id
    """

    def to_sql(self) -> str:
        return _build_merge_tree_sql(
            "SharedMergeTree",
            order_by=self.order_by,
            primary_key=self.primary_key,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            ttl=self.ttl,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class SummingMergeTree(Engine):
    """[`SummingMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/summingmergetree) engine for pre-aggregating data.

    Automatically sums values with the same sorting key.
    Useful for maintaining aggregated data incrementally.

    Args:
        columns: Columns to sum (optional).
        order_by: Sorting key expression.
        partition_by: Partition key expression.
        sample_by: Sampling expression.
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = SummingMergeTree(columns="amount", order_by="id")
        >>> print(engine)
        SummingMergeTree(amount) ORDER BY id
    """

    columns: str | None = None
    order_by: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        args = [self.columns] if self.columns else None
        return _build_merge_tree_sql(
            "SummingMergeTree",
            args=args,
            order_by=self.order_by,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class AggregatingMergeTree(Engine):
    """[`AggregatingMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/aggregatingmergetree) engine for pre-aggregating with aggregate functions.

    Stores data using AggregateFunction columns. Supports custom
    aggregation functions for incremental computation.

    Args:
        order_by: Sorting key expression.
        partition_by: Partition key expression.
        sample_by: Sampling expression.
        ttl: TTL expression for automatic data expiration.
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = AggregatingMergeTree(order_by="id")
        >>> print(engine)
        AggregatingMergeTree ORDER BY id
    """

    order_by: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    ttl: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        return _build_merge_tree_sql(
            "AggregatingMergeTree",
            order_by=self.order_by,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            ttl=self.ttl,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class ReplacingMergeTree(Engine):
    """[`ReplacingMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/replacingmergetree) engine for deduplication.

    Removes duplicate entries with the same sorting key, keeping
    only the latest or a specific version.

    Args:
        ver: Version column to select which row to keep.
        order_by: Sorting key expression.
        primary_key: Primary key expression.
        partition_by: Partition key expression.
        sample_by: Sampling expression.
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = ReplacingMergeTree(ver="version", order_by="id")
        >>> print(engine)
        ReplacingMergeTree(version) ORDER BY id
    """

    ver: str | None = None
    order_by: str | None = None
    primary_key: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        args = [self.ver] if self.ver else None
        return _build_merge_tree_sql(
            "ReplacingMergeTree",
            args=args,
            order_by=self.order_by,
            primary_key=self.primary_key,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class CollapsingMergeTree(Engine):
    """[`CollapsingMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/collapsingmergetree) engine for incremental calculation.

    Deduplicates data based on a sign column. Rows with opposite
    signs cancel each other out.

    Args:
        sign: Sign column name (typically 'sign' with values 1 and -1).
        order_by: Sorting key expression.
        partition_by: Partition key expression.
        sample_by: Sampling expression.
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = CollapsingMergeTree(sign="sign", order_by="id")
        >>> print(engine)
        CollapsingMergeTree(sign) ORDER BY id
    """

    sign: str
    order_by: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        return _build_merge_tree_sql(
            "CollapsingMergeTree",
            args=[self.sign],
            order_by=self.order_by,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class VersionedCollapsingMergeTree(Engine):
    """[`VersionedCollapsingMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/versionedcollapsingmergetree) for incremental calculation with versions.

    Similar to CollapsingMergeTree but uses a version column for
    better handling of concurrent writes.

    Args:
        sign: Sign column name.
        version: Version column name.
        order_by: Sorting key expression.
        partition_by: Partition key expression.
        sample_by: Sampling expression.
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = VersionedCollapsingMergeTree(sign="sign", version="ver", order_by="id")
        >>> print(engine)
        VersionedCollapsingMergeTree(sign, ver) ORDER BY id
    """

    sign: str
    version: str
    order_by: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        return _build_merge_tree_sql(
            "VersionedCollapsingMergeTree",
            args=[self.sign, self.version],
            order_by=self.order_by,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class GraphiteMergeTree(Engine):
    """[`GraphiteMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/graphitemergetree) engine for storing Graphite data.

    Optimized for storing and querying Graphite monitoring data
    with automatic data rollup support.

    Args:
        config_section: Configuration section name in graphite.config.
        order_by: Sorting key expression.
        primary_key: Primary key expression.
        partition_by: Partition key expression.
        sample_by: Sampling expression.
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = GraphiteMergeTree(config_section="graphite_config", order_by="path")
        >>> print(engine)
        GraphiteMergeTree(graphite_config) ORDER BY path
    """

    config_section: str
    order_by: str | None = None
    primary_key: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        return _build_merge_tree_sql(
            "GraphiteMergeTree",
            args=[self.config_section],
            order_by=self.order_by,
            primary_key=self.primary_key,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class CoalescingMergeTree(Engine):
    """[`CoalescingMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/coalescingmergetree) engine for coalescing identical rows.

    Merges rows that have identical values in specified columns.

    Args:
        columns: Columns to check for identical values.
        order_by: Sorting key expression.
        partition_by: Partition key expression.
        sample_by: Sampling expression.
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = CoalescingMergeTree(columns="col1", order_by="id")
        >>> print(engine)
        CoalescingMergeTree(col1) ORDER BY id
    """

    columns: str | None = None
    order_by: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        args = [self.columns] if self.columns else None
        return _build_merge_tree_sql(
            "CoalescingMergeTree",
            args=args,
            order_by=self.order_by,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


# Replicated engines


@dataclass(kw_only=True)
class ReplicatedMergeTree(Engine):
    """[`ReplicatedMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/replication) engine with ZooKeeper-based replication.

    Provides data replication across multiple servers using ZooKeeper
    for coordination. Supports automatic recovery and replica failover.

    Args:
        zk_path: ZooKeeper path for replica coordination.
        replica: Replica name in ZooKeeper.
        order_by: Sorting key expression. Defaults to 'tuple()'.
        primary_key: Primary key expression.
        partition_by: Partition key expression.
        sample_by: Sampling expression.
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = ReplicatedMergeTree(zk_path="/clickhouse/tables/mytable", replica="replica1")
        >>> print(engine)
        ReplicatedMergeTree('/clickhouse/tables/mytable', 'replica1') ORDER BY tuple()
    """

    zk_path: str | None = None
    replica: str | None = None
    order_by: str = "tuple()"
    primary_key: str | None = None
    partition_by: str | None = None
    sample_by: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        args = (
            [f"'{self.zk_path}'", f"'{self.replica}'"]
            if self.zk_path and self.replica
            else None
        )
        return _build_merge_tree_sql(
            "ReplicatedMergeTree",
            args=args,
            order_by=self.order_by,
            primary_key=self.primary_key,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class ReplicatedAggregatingMergeTree(ReplicatedMergeTree):
    """[`ReplicatedAggregatingMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/replication) for replicated pre-aggregation.

    Combines replication with aggregating merge tree functionality.

    Examples:
        >>> engine = ReplicatedAggregatingMergeTree(zk_path="/clickhouse/tables/mytable", replica="replica1", order_by="id")
        >>> print(engine)
        ReplicatedAggregatingMergeTree('/clickhouse/tables/mytable', 'replica1') ORDER BY id
    """

    def to_sql(self) -> str:
        args = (
            [f"'{self.zk_path}'", f"'{self.replica}'"]
            if self.zk_path and self.replica
            else None
        )
        return _build_merge_tree_sql(
            "ReplicatedAggregatingMergeTree",
            args=args,
            order_by=self.order_by,
            primary_key=self.primary_key,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class ReplicatedSummingMergeTree(ReplicatedMergeTree):
    """[`ReplicatedSummingMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/replication) for replicated pre-summarization.

    Combines replication with summing merge tree functionality.

    Examples:
        >>> engine = ReplicatedSummingMergeTree(zk_path="/clickhouse/tables/mytable", replica="replica1", order_by="id")
        >>> print(engine)
        ReplicatedSummingMergeTree('/clickhouse/tables/mytable', 'replica1') ORDER BY id
    """

    def to_sql(self) -> str:
        args = (
            [f"'{self.zk_path}'", f"'{self.replica}'"]
            if self.zk_path and self.replica
            else None
        )
        return _build_merge_tree_sql(
            "ReplicatedSummingMergeTree",
            args=args,
            order_by=self.order_by,
            primary_key=self.primary_key,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


# Shared variants


@dataclass(kw_only=True)
class SharedReplacingMergeTree(ReplacingMergeTree):
    """[`SharedReplacingMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/sharedmergetree) with shared metadata.

    Combines shared metadata with replacing merge tree functionality.

    Examples:
        >>> engine = SharedReplacingMergeTree(order_by="id")
        >>> print(engine)
        SharedReplacingMergeTree ORDER BY id
    """

    def to_sql(self) -> str:
        args = [self.ver] if self.ver else None
        return _build_merge_tree_sql(
            "SharedReplacingMergeTree",
            args=args,
            order_by=self.order_by,
            primary_key=self.primary_key,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class SharedAggregatingMergeTree(AggregatingMergeTree):
    """[`SharedAggregatingMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/sharedmergetree) with shared metadata.

    Combines shared metadata with aggregating merge tree functionality.

    Examples:
        >>> engine = SharedAggregatingMergeTree(order_by="id")
        >>> print(engine)
        SharedAggregatingMergeTree ORDER BY id
    """

    def to_sql(self) -> str:
        return _build_merge_tree_sql(
            "SharedAggregatingMergeTree",
            order_by=self.order_by,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            ttl=self.ttl,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class SharedSummingMergeTree(SummingMergeTree):
    """[`SharedSummingMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/sharedmergetree) with shared metadata.

    Combines shared metadata with summing merge tree functionality.

    Examples:
        >>> engine = SharedSummingMergeTree(columns="amount", order_by="id")
        >>> print(engine)
        SharedSummingMergeTree(amount) ORDER BY id
    """

    def to_sql(self) -> str:
        args = [self.columns] if self.columns else None
        return _build_merge_tree_sql(
            "SharedSummingMergeTree",
            args=args,
            order_by=self.order_by,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class SharedVersionedCollapsingMergeTree(VersionedCollapsingMergeTree):
    """[`SharedVersionedCollapsingMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/sharedmergetree) with shared metadata.

    Combines shared metadata with versioned collapsing merge tree functionality.

    Examples:
        >>> engine = SharedVersionedCollapsingMergeTree(sign="sign", version="ver", order_by="id")
        >>> print(engine)
        SharedVersionedCollapsingMergeTree(sign, ver) ORDER BY id
    """

    def to_sql(self) -> str:
        return _build_merge_tree_sql(
            "SharedVersionedCollapsingMergeTree",
            args=[self.sign, self.version],
            order_by=self.order_by,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


@dataclass(kw_only=True)
class SharedGraphiteMergeTree(GraphiteMergeTree):
    """[`SharedGraphiteMergeTree`](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/sharedmergetree) with shared metadata.

    Combines shared metadata with graphite merge tree functionality.

    Examples:
        >>> engine = SharedGraphiteMergeTree(config_section="graphite_config", order_by="path")
        >>> print(engine)
        SharedGraphiteMergeTree(graphite_config) ORDER BY path
    """

    def to_sql(self) -> str:
        return _build_merge_tree_sql(
            "SharedGraphiteMergeTree",
            args=[self.config_section],
            order_by=self.order_by,
            primary_key=self.primary_key,
            partition_by=self.partition_by,
            sample_by=self.sample_by,
            settings=self.settings,
        )


# integrations


@dataclass(kw_only=True)
class Kafka(Engine):
    """[`Kafka`](https://clickhouse.com/docs/en/engines/table-engines/integrations/kafka) engine for reading from Kafka topics.

    Allows ClickHouse to read data from Kafka streams. Can be used
    for real-time data ingestion from Kafka.

    Args:
        broker_list: Kafka broker addresses (comma-separated if multiple).
        topic_list: Kafka topic or topics to read from.
        group_name: Consumer group name.
        format: Message format (e.g., 'JSONEachRow', 'CSV', 'Avro').
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = Kafka(broker_list="localhost:9092", topic_list="my_topic", group_name="my_group", format="JSONEachRow")
        >>> print(engine)
        Kafka('localhost:9092', 'my_topic', 'my_group', 'JSONEachRow')
    """

    broker_list: str
    topic_list: str
    group_name: str
    format: str
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        parts = [
            f"Kafka('{self.broker_list}', '{self.topic_list}', '{self.group_name}', '{self.format}')"
        ]
        if self.settings:
            parts.append(comma_join(self.settings, prefix="SETTINGS"))
        return " ".join(parts)


@dataclass(kw_only=True)
class PostgreSQL(Engine):
    """[`PostgreSQL`](https://clickhouse.com/docs/en/engines/table-engines/integrations/postgresql) engine for reading from PostgreSQL tables.

    Allows ClickHouse to query data from PostgreSQL tables directly.
    Useful for data federation and migration scenarios.

    Args:
        host_port: PostgreSQL host and port (e.g., 'localhost:5432').
        database: PostgreSQL database name.
        table: PostgreSQL table name.
        user: PostgreSQL user name.
        password: PostgreSQL user password.
        schema: PostgreSQL schema name (optional, defaults to 'public').
        settings: Optional engine settings as a dictionary.

    Examples:
        >>> engine = PostgreSQL(host_port="localhost:5432", database="mydb", table="users", user="admin", password="secret")
        >>> print(engine)
        PostgreSQL('localhost:5432', 'mydb', 'users', 'admin', 'secret')
    """

    host_port: str
    database: str
    table: str
    user: str
    password: str
    schema: str | None = None
    settings: dict[str, Any] | None = None

    def to_sql(self) -> str:
        args = [
            f"'{self.host_port}'",
            f"'{self.database}'",
            f"'{self.table}'",
            f"'{self.user}'",
            f"'{self.password}'",
        ]
        if self.schema:
            args.append(f"'{self.schema}'")
        return _base_sql("PostgreSQL", args=args, settings=self.settings)


def build_engine(full_engine: str) -> Engine | None:
    """Factory function to create Engine from ClickHouse full_engine expression.

    This is an alias for Engine.from_sql() for backwards compatibility.

    Args:
        full_engine: The full engine SQL string.

    Returns:
        An Engine instance or None if the engine type is unknown.
    """
    return Engine.from_sql(full_engine)
