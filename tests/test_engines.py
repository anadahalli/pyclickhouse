from pyclickhouse import engines


def assert_engine(engine, expected: str) -> None:
    assert str(engine) == expected


class TestSimpleEngines:
    def test_memory(self) -> None:
        assert_engine(engines.Memory(), "Memory")
        assert_engine(
            engines.Memory(settings={"min_bytes_to_keep": 4096}),
            "Memory SETTINGS min_bytes_to_keep = 4096",
        )

    def test_null(self) -> None:
        assert_engine(engines.Null(), "Null")

    def test_log(self) -> None:
        assert_engine(engines.Log(), "Log")
        assert_engine(
            engines.Log(settings={"max_column_size": 8192}),
            "Log SETTINGS max_column_size = 8192",
        )

    def test_stripe_log(self) -> None:
        assert_engine(engines.StripeLog(), "StripeLog")
        assert_engine(
            engines.StripeLog(settings={"some_setting": 1}),
            "StripeLog SETTINGS some_setting = 1",
        )

    def test_tiny_log(self) -> None:
        assert_engine(engines.TinyLog(), "TinyLog")
        assert_engine(
            engines.TinyLog(settings={"some_setting": 1}),
            "TinyLog SETTINGS some_setting = 1",
        )

    def test_set(self) -> None:
        assert_engine(engines.Set(), "Set")
        assert_engine(
            engines.Set(settings={"some_setting": 1}), "Set SETTINGS some_setting = 1"
        )


class TestEnginesWithArgs:
    def test_dictionary(self) -> None:
        assert_engine(engines.Dictionary(dictionary="my_dict"), "Dictionary('my_dict')")

    def test_merge(self) -> None:
        assert_engine(
            engines.Merge(db_name="mydb", tables_regexp=".*"), "Merge(mydb, '.*')"
        )

    def test_file(self) -> None:
        assert_engine(engines.File(fmt="CSV"), "File('CSV')")

    def test_distributed(self) -> None:
        assert_engine(
            engines.Distributed(cluster="mycluster", database="mydb", table="mytable"),
            "Distributed(mycluster, mydb, mytable)",
        )
        assert_engine(
            engines.Distributed(
                cluster="mycluster", database="mydb", table="mytable", sharding_key="id"
            ),
            "Distributed(mycluster, mydb, mytable, id)",
        )
        assert_engine(
            engines.Distributed(
                cluster="mycluster",
                database="mydb",
                table="mytable",
                policy_name="default",
            ),
            "Distributed(mycluster, mydb, mytable, default)",
        )


class TestMergeTreeFamily:
    def test_merge_tree(self) -> None:
        assert_engine(engines.MergeTree(), "MergeTree ORDER BY tuple()")
        assert_engine(engines.MergeTree(order_by="id"), "MergeTree ORDER BY id")
        assert_engine(
            engines.MergeTree(order_by="id", partition_by="id % 10"),
            "MergeTree ORDER BY id PARTITION BY id % 10",
        )
        assert_engine(
            engines.MergeTree(order_by="id", primary_key="id"),
            "MergeTree ORDER BY id PRIMARY KEY id",
        )
        assert_engine(
            engines.MergeTree(order_by="id", sample_by="id"),
            "MergeTree ORDER BY id SAMPLE BY id",
        )
        assert_engine(
            engines.MergeTree(order_by="id", ttl="timestamp + INTERVAL 1 DAY"),
            "MergeTree ORDER BY id TTL timestamp + INTERVAL 1 DAY",
        )
        assert_engine(
            engines.MergeTree(order_by="id", settings={"index_granularity": 8192}),
            "MergeTree ORDER BY id SETTINGS index_granularity = 8192",
        )

    def test_shared_merge_tree(self) -> None:
        assert_engine(engines.SharedMergeTree(), "SharedMergeTree ORDER BY tuple()")
        assert_engine(
            engines.SharedMergeTree(order_by="id"), "SharedMergeTree ORDER BY id"
        )

    def test_summing_merge_tree(self) -> None:
        assert_engine(engines.SummingMergeTree(), "SummingMergeTree")
        assert_engine(
            engines.SummingMergeTree(columns="amount"), "SummingMergeTree(amount)"
        )
        assert_engine(
            engines.SummingMergeTree(columns="amount", order_by="id"),
            "SummingMergeTree(amount) ORDER BY id",
        )

    def test_aggregating_merge_tree(self) -> None:
        assert_engine(engines.AggregatingMergeTree(), "AggregatingMergeTree")
        assert_engine(
            engines.AggregatingMergeTree(order_by="id"),
            "AggregatingMergeTree ORDER BY id",
        )
        assert_engine(
            engines.AggregatingMergeTree(
                order_by="id", ttl="timestamp + INTERVAL 1 DAY"
            ),
            "AggregatingMergeTree ORDER BY id TTL timestamp + INTERVAL 1 DAY",
        )

    def test_replacing_merge_tree(self) -> None:
        assert_engine(
            engines.ReplacingMergeTree(order_by="id"), "ReplacingMergeTree ORDER BY id"
        )
        assert_engine(
            engines.ReplacingMergeTree(ver="ver", order_by="id"),
            "ReplacingMergeTree(ver) ORDER BY id",
        )

    def test_collapsing_merge_tree(self) -> None:
        assert_engine(
            engines.CollapsingMergeTree(sign="sign_col", order_by="id"),
            "CollapsingMergeTree(sign_col) ORDER BY id",
        )

    def test_versioned_collapsing_merge_tree(self) -> None:
        assert_engine(
            engines.VersionedCollapsingMergeTree(
                sign="sign_col", version="ver_col", order_by="id"
            ),
            "VersionedCollapsingMergeTree(sign_col, ver_col) ORDER BY id",
        )

    def test_graphite_merge_tree(self) -> None:
        assert_engine(
            engines.GraphiteMergeTree(config_section="graphite_config", order_by="id"),
            "GraphiteMergeTree(graphite_config) ORDER BY id",
        )

    def test_coalescing_merge_tree(self) -> None:
        assert_engine(engines.CoalescingMergeTree(), "CoalescingMergeTree")
        assert_engine(
            engines.CoalescingMergeTree(columns="col1", order_by="id"),
            "CoalescingMergeTree(col1) ORDER BY id",
        )


class TestReplicatedEngines:
    def test_replicated_merge_tree(self) -> None:
        assert_engine(
            engines.ReplicatedMergeTree(), "ReplicatedMergeTree ORDER BY tuple()"
        )
        assert_engine(
            engines.ReplicatedMergeTree(zk_path="/clickhouse/path", replica="replica1"),
            "ReplicatedMergeTree('/clickhouse/path', 'replica1') ORDER BY tuple()",
        )
        assert_engine(
            engines.ReplicatedMergeTree(
                zk_path="/clickhouse/path", replica="replica1", order_by="id"
            ),
            "ReplicatedMergeTree('/clickhouse/path', 'replica1') ORDER BY id",
        )

    def test_replicated_aggregating_merge_tree(self) -> None:
        assert_engine(
            engines.ReplicatedAggregatingMergeTree(
                zk_path="/clickhouse/path", replica="replica1", order_by="id"
            ),
            "ReplicatedAggregatingMergeTree('/clickhouse/path', 'replica1') ORDER BY id",
        )

    def test_replicated_summing_merge_tree(self) -> None:
        assert_engine(
            engines.ReplicatedSummingMergeTree(
                zk_path="/clickhouse/path", replica="replica1", order_by="id"
            ),
            "ReplicatedSummingMergeTree('/clickhouse/path', 'replica1') ORDER BY id",
        )


class TestSharedEngines:
    def test_shared_replacing_merge_tree(self) -> None:
        assert_engine(
            engines.SharedReplacingMergeTree(order_by="id"),
            "SharedReplacingMergeTree ORDER BY id",
        )

    def test_shared_aggregating_merge_tree(self) -> None:
        assert_engine(
            engines.SharedAggregatingMergeTree(order_by="id"),
            "SharedAggregatingMergeTree ORDER BY id",
        )

    def test_shared_summing_merge_tree(self) -> None:
        assert_engine(
            engines.SharedSummingMergeTree(order_by="id"),
            "SharedSummingMergeTree ORDER BY id",
        )

    def test_shared_versioned_collapsing_merge_tree(self) -> None:
        assert_engine(
            engines.SharedVersionedCollapsingMergeTree(
                sign="sign_col", version="ver_col", order_by="id"
            ),
            "SharedVersionedCollapsingMergeTree(sign_col, ver_col) ORDER BY id",
        )

    def test_shared_graphite_merge_tree(self) -> None:
        assert_engine(
            engines.SharedGraphiteMergeTree(
                config_section="graphite_config", order_by="id"
            ),
            "SharedGraphiteMergeTree(graphite_config) ORDER BY id",
        )


class TestIntegrationEngines:
    def test_kafka(self) -> None:
        assert_engine(
            engines.Kafka(
                broker_list="localhost:9092",
                topic_list="my_topic",
                group_name="my_group",
                format="JSONEachRow",
            ),
            "Kafka('localhost:9092', 'my_topic', 'my_group', 'JSONEachRow')",
        )
        assert_engine(
            engines.Kafka(
                broker_list="localhost:9092",
                topic_list="my_topic",
                group_name="my_group",
                format="JSONEachRow",
                settings={"max_block_size": 1000},
            ),
            "Kafka('localhost:9092', 'my_topic', 'my_group', 'JSONEachRow') SETTINGS max_block_size = 1000",
        )

    def test_postgresql(self) -> None:
        assert_engine(
            engines.PostgreSQL(
                host_port="localhost:5432",
                database="mydb",
                table="users",
                user="admin",
                password="secret",
            ),
            "PostgreSQL('localhost:5432', 'mydb', 'users', 'admin', 'secret')",
        )
        assert_engine(
            engines.PostgreSQL(
                host_port="localhost:5432",
                database="mydb",
                table="users",
                user="admin",
                password="secret",
                schema="public",
            ),
            "PostgreSQL('localhost:5432', 'mydb', 'users', 'admin', 'secret', 'public')",
        )


class TestEngineRegistry:
    def test_engine_map_contains_all_engines(self) -> None:
        expected_engines = [
            "Memory",
            "Null",
            "Log",
            "StripeLog",
            "TinyLog",
            "Set",
            "Dictionary",
            "Merge",
            "File",
            "Distributed",
            "MergeTree",
            "SharedMergeTree",
            "SummingMergeTree",
            "AggregatingMergeTree",
            "ReplacingMergeTree",
            "CollapsingMergeTree",
            "VersionedCollapsingMergeTree",
            "GraphiteMergeTree",
            "CoalescingMergeTree",
            "ReplicatedMergeTree",
            "ReplicatedAggregatingMergeTree",
            "ReplicatedSummingMergeTree",
            "SharedReplacingMergeTree",
            "SharedAggregatingMergeTree",
            "SharedSummingMergeTree",
            "SharedVersionedCollapsingMergeTree",
            "SharedGraphiteMergeTree",
            "Kafka",
            "PostgreSQL",
        ]
        assert sorted(engines.engine_map.keys()) == sorted(expected_engines)

    def test_from_sql(self) -> None:
        engine = engines.Engine.from_sql("MergeTree ORDER BY id")
        assert engine is not None
        assert engine.name == "MergeTree"
        assert engine.full_engine == "MergeTree ORDER BY id"

        assert engines.Engine.from_sql("") is None
        assert engines.Engine.from_sql("UnknownEngine()") is None

    def test_build_engine(self) -> None:
        engine = engines.build_engine("MergeTree ORDER BY id")
        assert engine is not None
        assert engine.name == "MergeTree"
        assert engine.full_engine == "MergeTree ORDER BY id"

        assert engines.build_engine("") is None
        assert engines.build_engine("UnknownEngine()") is None
