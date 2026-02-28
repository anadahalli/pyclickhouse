from pyclickhouse import MergeTree


class TestEngine:
    def test_engine_merge_tree(self) -> None:
        base = MergeTree()
        assert base.to_sql() == "ENGINE = MergeTree() ORDER BY tuple()"

        order = MergeTree(order_by="id")
        assert order.to_sql() == "ENGINE = MergeTree() ORDER BY id"

        partition = MergeTree(order_by="id", partition_by="id")
        assert partition.to_sql() == "ENGINE = MergeTree() ORDER BY id PARTITION BY id"

        primary = MergeTree(order_by="id", primary_key="id")
        assert primary.to_sql() == "ENGINE = MergeTree() ORDER BY id PRIMARY KEY id"
