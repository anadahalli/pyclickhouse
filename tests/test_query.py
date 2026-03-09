import pytest
from pydantic import BaseModel

from pyclickhouse.fields import Aggregate, F
from pyclickhouse.query import Query
from pyclickhouse.table import Table


class TestQuery:
    def test_query(self) -> None:
        class Model(BaseModel):
            key: str
            val: int

        table = Table(Model)

        q = Query(table="test", database="db", schema="sc")
        assert q.pipeline == ["from sc.db.test"]
        assert str(q) == "SELECT * FROM sc.db.test"
        q = Query(table=table, database="db", schema="sc")
        assert str(q) == "SELECT * FROM sc.db.model"
        q = Query(table=table, schema="sc")
        assert str(q) == "SELECT * FROM sc.model"
        q = Query(table=table, database="db")
        assert str(q) == "SELECT * FROM db.model"

        # base
        q = Query(table)
        assert q.pipeline == ["from model"]
        assert str(q) == "SELECT * FROM model"

        # select
        with pytest.raises(ValueError):
            q.select()
        s = q.select(table.key)
        assert s.pipeline == ["from model", "select {key}"]
        assert str(s) == "SELECT `key` FROM model"
        s = q.select(table.val)
        assert s.pipeline == ["from model", "select {val}"]
        assert str(s) == "SELECT val FROM model"
        s = q.select(table.key, table.val)
        assert s.pipeline == ["from model", "select {key, val}"]
        assert str(s) == "SELECT `key`, val FROM model"
        s = q.select(value=table.val)
        assert s.pipeline == ["from model", "select {value = val}"]
        assert str(s) == "SELECT val AS value FROM model"
        s = q.select(table.key, value=table.val)
        assert s.pipeline == ["from model", "select {key, value = val}"]
        assert str(s) == "SELECT `key`, val AS value FROM model"

        # derive
        with pytest.raises(ValueError):
            q.derive()
        s = q.derive(new_value=table.val + 1)
        assert s.pipeline == ["from model", "derive {new_value = val + 1}"]
        assert str(s) == "SELECT *, val + 1 AS new_value FROM model"
        s = q.derive(new_value=table.val * 10)
        assert s.pipeline == ["from model", "derive {new_value = val * 10}"]
        assert str(s) == "SELECT *, val * 10 AS new_value FROM model"

        # sort
        with pytest.raises(ValueError):
            q.sort()
        s = q.sort(table.val)
        assert s.pipeline == ["from model", "sort {val}"]
        assert str(s) == "SELECT * FROM model ORDER BY val"
        s = q.sort(-table.val)
        assert s.pipeline == ["from model", "sort {-val}"]
        assert str(s) == "SELECT * FROM model ORDER BY val DESC"

        # take
        with pytest.raises(ValueError):
            q.take()
            q.take(1, start=1)
            q.take(1, end=10)
            q.take(1, start=1, end=10)
        s = q.take(1)
        assert s.pipeline == ["from model", "take 1"]
        assert str(s) == "SELECT * FROM model LIMIT 1"
        s = q.take(start=10)
        assert s.pipeline == ["from model", "take 10.."]
        assert str(s) == "SELECT * FROM model OFFSET 9"
        s = q.take(end=10)
        assert s.pipeline == ["from model", "take ..10"]
        assert str(s) == "SELECT * FROM model LIMIT 10"
        s = q.take(start=10, end=20)
        assert s.pipeline == ["from model", "take 10..20"]
        assert str(s) == "SELECT * FROM model LIMIT 11 OFFSET 9"

        # filter
        s = q.filter(table.val == 10)
        assert s.pipeline == ["from model", "filter (val == 10)"]
        assert str(s) == "SELECT * FROM model WHERE val = 10"
        s = q.filter(table.val != 10)
        assert s.pipeline == ["from model", "filter (val != 10)"]
        assert str(s) == "SELECT * FROM model WHERE val <> 10"
        s = q.filter(table.val >= 10)
        assert s.pipeline == ["from model", "filter (val >= 10)"]
        assert str(s) == "SELECT * FROM model WHERE val >= 10"
        s = q.filter((table.val == 10) | (table.val == 20))
        assert s.pipeline == ["from model", "filter (val == 10 || val == 20)"]
        assert str(s) == "SELECT * FROM model WHERE val = 10 OR val = 20"
        s = q.filter((table.key == "test") & (table.val == 10))
        assert s.pipeline == ["from model", "filter (key == 'test' && val == 10)"]
        assert str(s) == "SELECT * FROM model WHERE `key` = 'test' AND val = 10"

        # aggregate
        s = q.aggregate(F.count())
        assert s.pipeline == ["from model", "aggregate {s'count()'}"]
        assert str(s) == "SELECT count() FROM model"
        s = q.aggregate(F.count(table.val))
        assert s.pipeline == ["from model", "aggregate {s'count(val)'}"]
        assert str(s) == "SELECT count(val) FROM model"
        s = q.aggregate(total=F.sum(table.val))
        assert s.pipeline == ["from model", "aggregate {total = s'sum(val)'}"]
        assert str(s) == "SELECT sum(val) AS total FROM model"

        # group
        s = q.group(table.key)
        assert s.pipeline == ["from model", "group {key} (aggregate {})"]
        assert str(s) == "SELECT `key` FROM model GROUP BY `key`"
        s = q.group(value=table.val)
        assert s.pipeline == ["from model", "group {value = val} (aggregate {})"]
        assert str(s) == "SELECT val AS value FROM model GROUP BY val"
        s = q.group(table.key, Aggregate(F.count()))
        assert s.pipeline == ["from model", "group {key} (aggregate {s'count()'})"]
        assert str(s) == "SELECT `key`, count() FROM model GROUP BY `key`"
        s = q.group(table.key, total=Aggregate(F.sum(table.val)))
        assert s.pipeline == [
            "from model",
            "group {key} (aggregate {total = s'sum(val)'})",
        ]
        assert str(s) == "SELECT `key`, sum(val) AS total FROM model GROUP BY `key`"
        s = q.group(name=table.key, total=Aggregate(F.sum(table.val)))
        assert s.pipeline == [
            "from model",
            "group {name = key} (aggregate {total = s'sum(val)'})",
        ]
        assert (
            str(s)
            == "SELECT `key` AS name, sum(val) AS total FROM model GROUP BY `key`"
        )
