from typing import Annotated

import pytest

from pyclickhouse import Column, F, MergeTree, Query, Table, TableConfig


class TestQuery:
    def test_query_builder(self) -> None:
        class Model(Table):
            table_config = TableConfig(
                engine=MergeTree(order_by="value"),
                name="test_table",
            )

            name: Annotated[str, Column(type="String", name="name")]
            value: Annotated[int, Column(type="UInt32", name="value")]

        # base
        query = Query(Model)
        prql = "from test_table"
        sql = "SELECT * FROM test_table"
        assert query._build() == prql
        assert query._compile() == sql
        assert str(query) == sql

        # select
        query = Query(Model)
        query = query.select(Model.name, Model.value)
        prql = "from test_table | select {name, value}"
        sql = "SELECT name, value FROM test_table"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query = query.select(Model.name, val=Model.value)
        prql = "from test_table | select {name, val = value}"
        sql = "SELECT name, value AS val FROM test_table"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query = query.select()
        prql = "from test_table"
        sql = "SELECT * FROM test_table"
        assert query._build() == prql
        assert query._compile() == sql

        # derive
        query = Query(Model)
        query = query.derive(new_name=Model.name, new_value=Model.value + 10)
        prql = "from test_table | derive {new_name = name, new_value = value + 10}"
        sql = "SELECT *, name AS new_name, value + 10 AS new_value FROM test_table"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query.select(Model.name)
        query = query.derive(new_name=Model.name)
        prql = "from test_table | select {name} | derive {new_name = name}"
        sql = "SELECT name, name AS new_name FROM test_table"
        assert query._build() == prql
        assert query._compile() == sql

        # filter
        query = Query(Model)
        query.filter(Model.value > 10)
        prql = "from test_table | filter (value > 10)"
        sql = "SELECT * FROM test_table WHERE value > 10"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query.filter(Model.name == "test")
        prql = 'from test_table | filter (name == "test")'
        sql = "SELECT * FROM test_table WHERE name = 'test'"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query.filter(Model.name == "test")
        query.filter(Model.value > 10)
        prql = 'from test_table | filter (name == "test") | filter (value > 10)'
        sql = "SELECT * FROM test_table WHERE name = 'test' AND value > 10"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query.filter(F.count(Model.value) > 10)
        prql = 'from test_table | filter (s"count(value)" > 10)'
        sql = "SELECT * FROM test_table WHERE count(value) > 10"
        assert query._build() == prql
        assert query._compile() == sql

        # TODO: AND & OR

        # sort
        query = Query(Model)
        query.sort(Model.name)
        prql = "from test_table | sort {name}"
        sql = "SELECT * FROM test_table ORDER BY name"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query.sort(Model.name, Model.value)
        prql = "from test_table | sort {name, value}"
        sql = "SELECT * FROM test_table ORDER BY name, value"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query.sort(-Model.value)
        prql = "from test_table | sort {-value}"
        sql = "SELECT * FROM test_table ORDER BY value DESC"
        assert query._build() == prql
        assert query._compile() == sql

        # take
        with pytest.raises(ValueError):
            Query(Model).take()
            Query(Model).take(10, start=100)
            Query(Model).take(10, end=100)
            Query(Model).take(10, start=10, end=100)

        query = Query(Model)
        query.take(1)
        prql = "from test_table | take 1"
        sql = "SELECT * FROM test_table LIMIT 1"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query.take(start=10)
        prql = "from test_table | take 10.."
        sql = "SELECT * FROM test_table OFFSET 9"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query.take(end=10)
        prql = "from test_table | take ..10"
        sql = "SELECT * FROM test_table LIMIT 10"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query.take(start=10, end=20)
        prql = "from test_table | take 10..20"
        sql = "SELECT * FROM test_table LIMIT 11 OFFSET 9"
        assert query._build() == prql
        assert query._compile() == sql

        # aggregate
        query = Query(Model)
        query.aggregate(F.avg(Model.value))
        prql = 'from test_table | aggregate {s"avg(value)"}'
        sql = "SELECT avg(value) FROM test_table"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query.aggregate(val=F.avg(Model.value))
        prql = 'from test_table | aggregate {val = s"avg(value)"}'
        sql = "SELECT avg(value) AS val FROM test_table"
        assert query._build() == prql
        assert query._compile() == sql

        # group
        query = Query(Model)
        query.group(Model.name, val=F.avg(Model.value))
        prql = 'from test_table | group {name} (aggregate {val = s"avg(value)"})'
        sql = "SELECT name, avg(value) AS val FROM test_table GROUP BY name"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query.group(n=Model.name, val=F.avg(Model.value))
        prql = 'from test_table | group {n = name} (aggregate {val = s"avg(value)"})'
        sql = "SELECT name AS n, avg(value) AS val FROM test_table GROUP BY name"
        assert query._build() == prql
        assert query._compile() == sql

        query = Query(Model)
        query.group(Model.name, F.avg(Model.value))
        prql = 'from test_table | group {name} (aggregate {s"avg(value)"})'
        sql = "SELECT name, avg(value) FROM test_table GROUP BY name"
        assert query._build() == prql
        assert query._compile() == sql

        # window
