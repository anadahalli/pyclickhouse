import pytest
from pydantic import BaseModel

from pyclickhouse.fields import Aggregate, Param
from pyclickhouse.functions import F
from pyclickhouse.query import Query
from pyclickhouse.table import Table


class Model(BaseModel):
    name: str
    value: int


table = Table(Model, name="model")


class TestQuery:
    def test_query_base(self) -> None:
        # base
        q = Query(table)
        assert q.pipeline == ["from model"]
        assert str(q) == "SELECT * FROM model"

    def test_query_select(self) -> None:
        q = Query(table)
        # select
        with pytest.raises(ValueError):
            q.select()
        s = q.select(table.name)
        assert s.pipeline == ["from model", "select {model.name}"]
        assert str(s) == "SELECT name FROM model"
        s = q.select(table.value)
        assert s.pipeline == ["from model", "select {model.value}"]
        assert str(s) == "SELECT value FROM model"
        s = q.select(table.name, table.value)
        assert s.pipeline == ["from model", "select {model.name, model.value}"]
        assert str(s) == "SELECT name, value FROM model"
        s = q.select(val=table.value)
        assert s.pipeline == ["from model", "select {val = model.value}"]
        assert str(s) == "SELECT value AS val FROM model"
        s = q.select(table.name, val=table.value)
        assert s.pipeline == ["from model", "select {model.name, val = model.value}"]
        assert str(s) == "SELECT name, value AS val FROM model"

    def test_query_derive(self) -> None:
        q = Query(table)
        # derive
        with pytest.raises(ValueError):
            q.derive()
        s = q.derive(new_value=table.value + 1)
        assert s.pipeline == ["from model", "derive {new_value = model.value + 1}"]
        assert str(s) == "SELECT *, value + 1 AS new_value FROM model"
        s = q.derive(new_value=table.value * 10)
        assert s.pipeline == ["from model", "derive {new_value = model.value * 10}"]
        assert str(s) == "SELECT *, value * 10 AS new_value FROM model"

    def test_query_sort(self) -> None:
        q = Query(table)
        # sort
        with pytest.raises(ValueError):
            q.sort()
        s = q.sort(table.value)
        assert s.pipeline == ["from model", "sort {model.value}"]
        assert str(s) == "SELECT * FROM model ORDER BY value"
        s = q.sort(-table.value)
        assert s.pipeline == ["from model", "sort {-model.value}"]
        assert str(s) == "SELECT * FROM model ORDER BY value DESC"

    def test_query_take(self) -> None:
        q = Query(table)
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

    def test_query_filter(self) -> None:
        q = Query(table)
        # filter
        s = q.filter(table.value == 10)
        assert s.pipeline == ["from model", "filter (model.value == 10)"]
        assert str(s) == "SELECT * FROM model WHERE value = 10"
        s = q.filter(table.value != 10)
        assert s.pipeline == ["from model", "filter (model.value != 10)"]
        assert str(s) == "SELECT * FROM model WHERE value <> 10"
        s = q.filter(table.value >= 10)
        assert s.pipeline == ["from model", "filter (model.value >= 10)"]
        assert str(s) == "SELECT * FROM model WHERE value >= 10"
        s = q.filter((table.value == 10) | (table.value == 20))
        assert s.pipeline == [
            "from model",
            "filter (model.value == 10 || model.value == 20)",
        ]
        assert str(s) == "SELECT * FROM model WHERE value = 10 OR value = 20"
        s = q.filter((table.name == "test") & (table.value == 10))
        assert s.pipeline == [
            "from model",
            "filter (model.name == 'test' && model.value == 10)",
        ]
        assert str(s) == "SELECT * FROM model WHERE name = 'test' AND value = 10"
        s = q.filter(table.value.is_in([1, 2, 3]))
        assert s.pipeline == ["from model", "filter ((model.value | in [1, 2, 3]))"]
        assert str(s) == "SELECT * FROM model WHERE value IN (1, 2, 3)"
        s = q.filter(table.value.is_not_in([1, 2, 3]))
        assert s.pipeline == ["from model", "filter (!(model.value | in [1, 2, 3]))"]
        assert str(s) == "SELECT * FROM model WHERE NOT value IN (1, 2, 3)"

    def test_query_aggregate(self) -> None:
        q = Query(table)
        # aggregate
        s = q.aggregate(F.count())
        assert s.pipeline == ["from model", "aggregate {s'count()'}"]
        assert str(s) == "SELECT count() FROM model"
        s = q.aggregate(F.count(table.value))
        assert s.pipeline == ["from model", "aggregate {s'count(model.value)'}"]
        assert str(s) == "SELECT count(model.value) FROM model"
        s = q.aggregate(total=F.sum(table.value))
        assert s.pipeline == ["from model", "aggregate {total = s'sum(model.value)'}"]
        assert str(s) == "SELECT sum(model.value) AS total FROM model"

    def test_query_group(self) -> None:
        q = Query(table)
        # group
        s = q.group(table.name)
        assert s.pipeline == ["from model", "group {model.name} (aggregate {})"]
        assert str(s) == "SELECT name FROM model GROUP BY name"
        s = q.group(val=table.value)
        assert s.pipeline == ["from model", "group {val = model.value} (aggregate {})"]
        assert str(s) == "SELECT value AS val FROM model GROUP BY value"
        s = q.group(table.name, Aggregate(F.count()))
        assert s.pipeline == [
            "from model",
            "group {model.name} (aggregate {s'count()'})",
        ]
        assert str(s) == "SELECT name, count() FROM model GROUP BY name"
        s = q.group(table.name, total=Aggregate(F.sum(table.value)))
        assert s.pipeline == [
            "from model",
            "group {model.name} (aggregate {total = s'sum(model.value)'})",
        ]
        assert (
            str(s) == "SELECT name, sum(model.value) AS total FROM model GROUP BY name"
        )
        s = q.group(name=table.name, total=Aggregate(F.sum(table.value)))
        assert s.pipeline == [
            "from model",
            "group {name = model.name} (aggregate {total = s'sum(model.value)'})",
        ]
        assert (
            str(s) == "SELECT name, sum(model.value) AS total FROM model GROUP BY name"
        )

    def test_query_params(self) -> None:
        q = Query(table)
        # params
        q = Query(table)
        s = q.filter(table.value >= Param("value", int))
        assert s.pipeline == [
            "from model",
            "filter (model.value >= s'{{value:Int64}}')",
        ]
        assert str(s) == "SELECT * FROM model WHERE value >= {value:Int64}"
        s = q.filter(table.name == Param("name"))
        assert s.pipeline == ["from model", "filter (model.name == s'{{name:String}}')"]
        assert str(s) == "SELECT * FROM model WHERE name = {name:String}"
