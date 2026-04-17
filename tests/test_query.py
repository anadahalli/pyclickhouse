import pytest
from pydantic import BaseModel

from pyclickhouse.fields import Aggregate, Param, Window
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

    def test_query_join(self) -> None:
        q = Query(table)
        other = Table(Model, name="other")

        # default join
        s = q.join(other, (table.name == other.name))
        assert s.pipeline == [
            "from model",
            "join side:inner other (model.name == other.name)",
        ]
        assert (
            str(s)
            == "SELECT model.*, other.* FROM model INNER JOIN other ON model.name = other.name"
        )

        # inner join
        s = q.join(other, (table.name == other.name), side="inner")
        assert s.pipeline == [
            "from model",
            "join side:inner other (model.name == other.name)",
        ]
        assert (
            str(s)
            == "SELECT model.*, other.* FROM model INNER JOIN other ON model.name = other.name"
        )

        # left join
        s = q.join(other, (table.name == other.name), side="left")
        assert s.pipeline == [
            "from model",
            "join side:left other (model.name == other.name)",
        ]
        assert (
            str(s)
            == "SELECT model.*, other.* FROM model LEFT OUTER JOIN other ON model.name = other.name"
        )

        # full join
        s = q.join(other, (table.name == other.name), side="full")
        assert s.pipeline == [
            "from model",
            "join side:full other (model.name == other.name)",
        ]
        assert (
            str(s)
            == "SELECT model.*, other.* FROM model FULL JOIN other ON model.name = other.name"
        )

        # right join
        s = q.join(other, (table.name == other.name), side="right")
        assert s.pipeline == [
            "from model",
            "join side:right other (model.name == other.name)",
        ]
        assert (
            str(s)
            == "SELECT model.*, other.* FROM model RIGHT OUTER JOIN other ON model.name = other.name"
        )

        # join with string relation
        s = q.join("other", (table.name == other.name))
        assert s.pipeline == [
            "from model",
            "join side:inner other (model.name == other.name)",
        ]
        assert (
            str(s)
            == "SELECT model.*, other.* FROM model INNER JOIN other ON model.name = other.name"
        )

        # join chained with other operations
        s = q.join(other, (table.name == other.name)).filter(table.value > 10)
        assert s.pipeline == [
            "from model",
            "join side:inner other (model.name == other.name)",
            "filter (model.value > 10)",
        ]
        assert (
            str(s)
            == "SELECT model.*, other.* FROM model INNER JOIN other ON model.name = other.name WHERE model.value > 10"
        )

        # multiple joins
        other2 = Table(Model, name="other2")
        s = q.join(other, (table.name == other.name)).join(
            other2, (table.value == other2.value)
        )
        assert s.pipeline == [
            "from model",
            "join side:inner other (model.name == other.name)",
            "join side:inner other2 (model.value == other2.value)",
        ]
        assert (
            str(s)
            == "SELECT model.*, other.*, other2.* FROM model INNER JOIN other ON model.name = other.name INNER JOIN other2 ON model.value = other2.value"
        )

        # join with select
        s = q.join(other, (table.name == other.name)).select(table.name, other.value)
        assert s.pipeline == [
            "from model",
            "join side:inner other (model.name == other.name)",
            "select {model.name, other.value}",
        ]
        assert (
            str(s)
            == "SELECT model.name, other.value FROM model INNER JOIN other ON model.name = other.name"
        )

        # join with multiple conditions
        s = q.join(other, (table.name == other.name) & (table.value == other.value))
        assert s.pipeline == [
            "from model",
            "join side:inner other (model.name == other.name && model.value == other.value)",
        ]
        assert (
            str(s)
            == "SELECT model.*, other.* FROM model INNER JOIN other ON model.name = other.name AND model.value = other.value"
        )

    def test_query_exclude(self) -> None:
        q = Query(table)

        # exclude with select
        s = q.select(table.name, table.value).exclude(table.value)
        assert s.pipeline == [
            "from model",
            "select {model.name, model.value}",
            "select !{model.value}",
        ]
        assert str(s) == "SELECT name FROM model"

        # exclude with group
        s = q.group(table.name, val=Aggregate(F.count(table.value))).exclude(table.name)
        assert s.pipeline == [
            "from model",
            "group {model.name} (aggregate {val = s'count(model.value)'})",
            "select !{model.name}",
        ]
        assert str(s) == "SELECT count(model.value) AS val FROM model GROUP BY name"

    def test_query_group_with_window(self) -> None:
        q = Query(table)

        # group with window - range
        s = q.group(
            table.name,
            Window(range=(-2, 0)),
            total=Aggregate(F.count(table.value)),
        )
        assert s.pipeline == [
            "from model",
            "group {model.name} (aggregate {total = s'count(model.value) OVER (RANGE BETWEEN 2 PRECEDING AND CURRENT ROW)'})",
        ]
        assert (
            str(s)
            == "SELECT name, count(model.value) OVER (RANGE BETWEEN 2 PRECEDING AND CURRENT ROW) AS total FROM model GROUP BY name"
        )

        # group with window - range with unbounded
        s = q.group(
            table.name,
            Window(range=(None, 1)),
            total=Aggregate(F.sum(table.value)),
        )
        assert s.pipeline == [
            "from model",
            "group {model.name} (aggregate {total = s'sum(model.value) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND 1 FOLLOWING)'})",
        ]
        assert (
            str(s)
            == "SELECT name, sum(model.value) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND 1 FOLLOWING) AS total FROM model GROUP BY name"
        )

        # group with window - rows
        s = q.group(
            table.name,
            Window(rows=(2, 4)),
            average=Aggregate(F.avg(table.value)),
        )
        assert s.pipeline == [
            "from model",
            "group {model.name} (aggregate {average = s'avg(model.value) OVER (ROWS BETWEEN 2 FOLLOWING AND 4 FOLLOWING)'})",
        ]
        assert (
            str(s)
            == "SELECT name, avg(model.value) OVER (ROWS BETWEEN 2 FOLLOWING AND 4 FOLLOWING) AS average FROM model GROUP BY name"
        )

        # group with window - rows with unbounded
        s = q.group(
            table.name,
            Window(rows=(-4, None)),
            average=Aggregate(F.avg(table.value)),
        )
        assert s.pipeline == [
            "from model",
            "group {model.name} (aggregate {average = s'avg(model.value) OVER (ROWS BETWEEN 4 PRECEDING AND UNBOUNDED FOLLOWING)'})",
        ]
        assert (
            str(s)
            == "SELECT name, avg(model.value) OVER (ROWS BETWEEN 4 PRECEDING AND UNBOUNDED FOLLOWING) AS average FROM model GROUP BY name"
        )

        # group with multiple aggregates and window
        s = q.group(
            table.name,
            Window(range=(0, 0)),
            count=Aggregate(F.count()),
            total=Aggregate(F.sum(table.value)),
        )
        assert s.pipeline == [
            "from model",
            "group {model.name} (aggregate {count = s'count() OVER (RANGE BETWEEN CURRENT ROW AND CURRENT ROW)', total = s'sum(model.value) OVER (RANGE BETWEEN CURRENT ROW AND CURRENT ROW)'})",
        ]

        # group with window but no aggregates should raise
        with pytest.raises(ValueError):
            q.group(
                table.name,
                Window(range=(0, 0)),
            )

        # group with multiple windows should raise
        with pytest.raises(ValueError):
            q.group(
                table.name,
                Window(range=(0, 0)),
                Window(rows=(1, 1)),
                total=Aggregate(F.count()),
            )

    def test_query_window(self) -> None:
        q = Query(table)

        with pytest.raises(ValueError):
            q.window(Window())

        with pytest.raises(ValueError):
            q.window(Window(range=(1, 2), rows=(1, 2)))

        # range
        s = q.window(
            Window(range=(-2, 0)),
            total=Aggregate(F.count(table.value)),
        )
        assert s.pipeline == [
            "from model",
            "derive {total = s'count(model.value) OVER (RANGE BETWEEN 2 PRECEDING AND CURRENT ROW)'}",
        ]
        assert (
            str(s)
            == "SELECT *, count(model.value) OVER (RANGE BETWEEN 2 PRECEDING AND CURRENT ROW) AS total FROM model"
        )

        s = q.window(
            Window(range=(None, 1)),
            total=Aggregate(F.count(table.value)),
        )
        assert s.pipeline == [
            "from model",
            "derive {total = s'count(model.value) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND 1 FOLLOWING)'}",
        ]
        assert (
            str(s)
            == "SELECT *, count(model.value) OVER (RANGE BETWEEN UNBOUNDED PRECEDING AND 1 FOLLOWING) AS total FROM model"
        )

        # rows
        s = q.window(
            Window(rows=(2, 4)),
            average=Aggregate(F.avg(table.value)),
        )
        assert s.pipeline == [
            "from model",
            "derive {average = s'avg(model.value) OVER (ROWS BETWEEN 2 FOLLOWING AND 4 FOLLOWING)'}",
        ]
        assert (
            str(s)
            == "SELECT *, avg(model.value) OVER (ROWS BETWEEN 2 FOLLOWING AND 4 FOLLOWING) AS average FROM model"
        )

        s = q.window(
            Window(rows=(-4, None)),
            average=Aggregate(F.avg(table.value)),
        )
        assert s.pipeline == [
            "from model",
            "derive {average = s'avg(model.value) OVER (ROWS BETWEEN 4 PRECEDING AND UNBOUNDED FOLLOWING)'}",
        ]
        assert (
            str(s)
            == "SELECT *, avg(model.value) OVER (ROWS BETWEEN 4 PRECEDING AND UNBOUNDED FOLLOWING) AS average FROM model"
        )
