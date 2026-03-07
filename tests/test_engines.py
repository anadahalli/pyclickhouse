from pyclickhouse import engines


class TestEngines:
    def test_memory(self) -> None:
        engine = engines.Memory()
        assert str(engine) == "Memory"
        engine = engines.Memory(settings={"min_bytes_to_keep": 4096})
        assert str(engine) == "Memory SETTINGS min_bytes_to_keep = 4096"

    def test_merge_tree(self) -> None:
        engine = engines.MergeTree()
        assert str(engine) == "MergeTree ORDER BY tuple()"
        engine = engines.MergeTree(order_by="id")
        assert str(engine) == "MergeTree ORDER BY id"
        engine = engines.MergeTree(order_by="id", partition_by="id")
        assert str(engine) == "MergeTree ORDER BY id PARTITION BY id"
        engine = engines.MergeTree(order_by="id", primary_key="id")
        assert str(engine) == "MergeTree ORDER BY id PRIMARY KEY id"
        engine = engines.MergeTree(order_by="id", sample_by="id")
        assert str(engine) == "MergeTree ORDER BY id SAMPLE BY id"
        engine = engines.MergeTree(order_by="id", ttl="id")
        assert str(engine) == "MergeTree ORDER BY id TTL id"
        engine = engines.MergeTree(order_by="id", settings={"index_granularity": 8192})
        assert str(engine) == "MergeTree ORDER BY id SETTINGS index_granularity = 8192"
