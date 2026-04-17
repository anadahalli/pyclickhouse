# Engines

This module provides ClickHouse table engine classes for use in table definitions.

::: engines.Engine

---

## Engine Reference

### Simple Engines

| Engine | Description | Required Args |
|--------|-------------|---------------|
| [Memory](#engines.Memory) | Stores data in RAM | - |
| [Null](#engines.Null) | Writes but discards data | - |
| [Log](#engines.Log) | Basic logging engine | - |
| [StripeLog](#engines.StripeLog) | Stripe-logged storage | - |
| [TinyLog](#engines.TinyLog) | Lightweight logging | - |
| [Set](#engines.Set) | Set storage | - |
| [Dictionary](#engines.Dictionary) | Dictionary engine | `dictionary` |
| [Merge](#engines.Merge) | Merge family tables | `db_name`, `tables_regexp` |
| [File](#engines.File) | File-based storage | `fmt` |
| [Distributed](#engines.Distributed) | Distributed tables | `cluster`, `database`, `table` |

### MergeTree Family

| Engine | Description | Required Args |
|--------|-------------|---------------|
| [MergeTree](#engines.MergeTree) | Main engine for storing and merging data | `order_by` |
| [SummingMergeTree](#engines.SummingMergeTree) | Pre-aggregating data | `order_by` |
| [AggregatingMergeTree](#engines.AggregatingMergeTree) | Pre-aggregating with aggregate functions | `order_by` |
| [ReplacingMergeTree](#engines.ReplacingMergeTree) | Deduplication | `order_by` |
| [CollapsingMergeTree](#engines.CollapsingMergeTree) | Incremental calculation | `sign`, `order_by` |
| [VersionedCollapsingMergeTree](#engines.VersionedCollapsingMergeTree) | Incremental calculation with versions | `sign`, `version`, `order_by` |
| [GraphiteMergeTree](#engines.GraphiteMergeTree) | Graphite data storage | `config_section`, `order_by` |
| [CoalescingMergeTree](#engines.CoalescingMergeTree) | Coalescing identical rows | `order_by` |
| [SharedMergeTree](#engines.SharedMergeTree) | Shared metadata | `order_by` |

### Replicated Engines

| Engine | Description | Required Args |
|--------|-------------|---------------|
| [ReplicatedMergeTree](#engines.ReplicatedMergeTree) | ZooKeeper-based replication | `order_by` |
| [ReplicatedAggregatingMergeTree](#engines.ReplicatedAggregatingMergeTree) | Replicated pre-aggregation | `order_by` |
| [ReplicatedSummingMergeTree](#engines.ReplicatedSummingMergeTree) | Replicated pre-summarization | `order_by` |

### Shared Variants

| Engine | Description | Required Args |
|--------|-------------|---------------|
| [SharedReplacingMergeTree](#engines.SharedReplacingMergeTree) | Shared replacing | `order_by` |
| [SharedAggregatingMergeTree](#engines.SharedAggregatingMergeTree) | Shared aggregating | `order_by` |
| [SharedSummingMergeTree](#engines.SharedSummingMergeTree) | Shared summing | `order_by` |
| [SharedVersionedCollapsingMergeTree](#engines.SharedVersionedCollapsingMergeTree) | Shared versioned collapsing | `order_by` |
| [SharedGraphiteMergeTree](#engines.SharedGraphiteMergeTree) | Shared graphite | `order_by` |

### Integration Engines

| Engine | Description | Required Args |
|--------|-------------|---------------|
| [Kafka](#engines.Kafka) | Kafka integration | `broker_list`, `topic_list`, `group_name`, `format` |
| [PostgreSQL](#engines.PostgreSQL) | PostgreSQL integration | `host_port`, `database`, `table`, `user`, `password` |

---

## Simple Engines

::: engines.Memory

::: engines.Null

::: engines.Log

::: engines.StripeLog

::: engines.TinyLog

::: engines.Set

::: engines.Dictionary

::: engines.Merge

::: engines.File

::: engines.Distributed

---

## MergeTree Family

::: engines.MergeTree

::: engines.SummingMergeTree

::: engines.AggregatingMergeTree

::: engines.ReplacingMergeTree

::: engines.CollapsingMergeTree

::: engines.VersionedCollapsingMergeTree

::: engines.GraphiteMergeTree

::: engines.CoalescingMergeTree

::: engines.SharedMergeTree

---

## Replicated Engines

::: engines.ReplicatedMergeTree

::: engines.ReplicatedAggregatingMergeTree

::: engines.ReplicatedSummingMergeTree

---

## Shared Variants

::: engines.SharedReplacingMergeTree

::: engines.SharedAggregatingMergeTree

::: engines.SharedSummingMergeTree

::: engines.SharedVersionedCollapsingMergeTree

::: engines.SharedGraphiteMergeTree

---

## Integration Engines

::: engines.Kafka

::: engines.PostgreSQL
