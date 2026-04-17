from enum import Enum
from typing import Annotated

import pytest
from pydantic import BaseModel
from pydantic.fields import FieldInfo

from pyclickhouse.fields import Aggregate, Column, Expression, Param, Window
from pyclickhouse.functions import F


class TestColumn:
    def test_column(self) -> None:
        with pytest.raises(ValueError):
            Column().to_sql()
            Column(name="test").to_sql()
            Column(type="String").to_sql()
            Column(type="String", name="test", default_type="DEFAULT")

        column = Column("String", "test")
        column.to_sql() == "test String"
        str(column) == "test"

        column = Column(
            "DateTime",
            "test",
            default_type="DEFAULT",
            default_expression="now()",
        )
        assert column.to_sql() == "test DateTime DEFAULT now()"

        column = Column(
            "DateTime",
            "test",
            codec_expression="ZSTD",
        )
        assert column.to_sql() == "test DateTime CODEC(ZSTD)"

        column = Column(
            "DateTime",
            "test",
            ttl_expression="now() + INTERVAL 1 MONTH",
        )
        assert column.to_sql() == "test DateTime TTL now() + INTERVAL 1 MONTH"

        column = Column(
            "DateTime",
            "test",
            default_type="DEFAULT",
            default_expression="now()",
            comment="test",
            codec_expression="ZSTD",
            ttl_expression="now() + INTERVAL 1 MONTH",
        )
        assert (
            column.to_sql()
            == "test DateTime DEFAULT now() COMMENT 'test' CODEC(ZSTD) TTL now() + INTERVAL 1 MONTH"
        )

    def test_from_field(self) -> None:
        info = FieldInfo(annotation=str)
        col = Column.from_field("test", info)
        assert col.name == "test"
        assert col.type == "String"

        class Model(BaseModel):
            test: Annotated[str, Column()]

        info = Model.model_fields["test"]
        col = Column.from_field("test", info)
        assert col.name == "test"
        assert col.type == "String"

        class Model(BaseModel):
            test: Annotated[str, Column(type="DateTime", name="field")]

        info = Model.model_fields["test"]
        col = Column.from_field("test", info)
        assert col.name == "field"
        assert col.type == "DateTime"

    def test_from_sql(self) -> None:
        sql = {
            "type": "String",
            "name": "name",
            "default_type": "DEFAULT",
            "default_expression": "now()",
            "comment": "test",
            "codec_expression": "ZSTD(1)",
            "ttl_expression": "now() + INTERVAL 1 MONTH",
        }
        assert Column.from_sql(**sql) == Column(
            name="name",
            type="String",
            default_type="DEFAULT",
            default_expression="now()",
            comment="test",
            codec_expression="ZSTD(1)",
            ttl_expression="now() + INTERVAL 1 MONTH",
        )

    def test_column_datatypes(self) -> None:
        # str
        c = Column.from_field("test", FieldInfo(annotation=str))
        assert c.type == "String"
        assert c.to_sql() == "test String"
        # int
        c = Column.from_field("test", FieldInfo(annotation=int | None))
        assert c.type == "Nullable(Int64)"
        assert c.to_sql() == "test Nullable(Int64)"
        # list
        c = Column.from_field("test", FieldInfo(annotation=list[str]))
        assert c.type == "Array(String)"
        assert c.to_sql() == "test Array(String)"
        # tuple
        c = Column.from_field("test", FieldInfo(annotation=tuple[str, int]))
        assert c.type == "Tuple(String, Int64)"
        assert c.to_sql() == "test Tuple(String, Int64)"
        # dict
        c = Column.from_field("test", FieldInfo(annotation=dict[str, int]))
        assert c.type == "Map(String, Int64)"
        assert c.to_sql() == "test Map(String, Int64)"

        # enum
        class States(Enum):
            open = 1
            closed = 2

        c = Column.from_field("test", FieldInfo(annotation=States))
        assert c.type == "Enum('open', 'closed')"
        assert c.to_sql() == "test Enum('open', 'closed')"

        # nested


class TestExpression:
    def test_expression(self) -> None:
        f = Expression("test")
        assert str(f) == "test"

        c = Column(type="String", name="name")
        e = Expression(c.name)
        assert str(e) == "name"

        # prefix
        assert str(-e) == "-name"
        assert str(+e) == "+name"

        # comparision
        assert str(e > 10) == "name > 10"
        assert str(e > f) == "name > test"
        assert str(e >= 10) == "name >= 10"
        assert str(e >= f) == "name >= test"
        assert str(e < 10) == "name < 10"
        assert str(e < f) == "name < test"
        assert str(e <= 10) == "name <= 10"
        assert str(e <= f) == "name <= test"
        assert str(e == 10) == "name == 10"
        assert str(e == f) == "name == test"
        assert str(e != 10) == "name != 10"
        assert str(e != f) == "name != test"

        # airthmetic
        assert str(e + 10) == "name + 10"
        assert str(e + f) == "name + test"
        assert str(e - 10) == "name - 10"
        assert str(e - f) == "name - test"
        assert str(e * 10) == "name * 10"
        assert str(e * f) == "name * test"
        assert str(e / 10) == "name / 10"
        assert str(e / f) == "name / test"

        # logical
        assert str(e & 10) == "name && 10"
        assert str(e & f) == "name && test"
        assert str(e | 10) == "name || 10"
        assert str(e | f) == "name || test"
        assert str(~e) == "!name"
        assert str(~f) == "!test"

        # contains
        assert str(e.is_in([1, 2, 3])) == "(name | in [1, 2, 3])"
        assert str(e.is_in(f)) == "(name | in test)"
        assert str(e.is_not_in([1, 2, 3])) == "!(name | in [1, 2, 3])"
        assert str(e.is_not_in(f)) == "!(name | in test)"


class TestFunction:
    def test_function(self) -> None:
        e = Expression("test")
        assert F.count(e).to_sql() == "s'count(test)'"
        assert F.toInt32(F.count(e)).to_sql() == "s'toInt32(count(test))'"


class TestAggregate:
    def test_aggregate_with_string(self) -> None:
        agg = Aggregate("value")
        assert str(agg) == "value"

    def test_aggregate_with_function(self) -> None:
        expr = Expression("value")
        agg = Aggregate(F.sum(expr))
        assert str(agg) == "s'sum(value)'"

    def test_aggregate_with_expression(self) -> None:
        expr = Expression("test_column")
        agg = Aggregate(F.count(expr))
        assert "count" in str(agg)
        assert "test_column" in str(agg)

    def test_aggregate_with_nested_function(self) -> None:
        expr = Expression("value")
        agg = Aggregate(F.toInt32(F.count(expr)))
        assert "toInt32" in str(agg)
        assert "count" in str(agg)


class TestParam:
    def test_param_with_default_type(self) -> None:
        param = Param("name")
        assert param.name == "name"
        assert param.type == "String"
        assert str(param) == "s'{{name:String}}'"

    def test_param_with_int_type(self) -> None:
        param = Param("value", int)
        assert param.name == "value"
        assert param.type == "Int64"
        assert str(param) == "s'{{value:Int64}}'"

    def test_param_with_float_type(self) -> None:
        param = Param("score", float)
        assert param.name == "score"
        assert param.type == "Float64"
        assert str(param) == "s'{{score:Float64}}'"

    def test_param_with_explicit_str_type(self) -> None:
        param = Param("username", str)
        assert param.name == "username"
        assert param.type == "String"
        assert str(param) == "s'{{username:String}}'"


class TestWindow:
    def test_window_validation_no_range_or_rows(self) -> None:
        with pytest.raises(ValueError):
            Window()

    def test_window_validation_both_range_and_rows(self) -> None:
        with pytest.raises(ValueError):
            Window(range=(1, 2), rows=(1, 2))

    def test_window_with_range(self) -> None:
        window = Window(range=(-2, 0))
        assert window.range == (-2, 0)
        assert window.rows is None
        assert "RANGE BETWEEN 2 PRECEDING AND CURRENT ROW" in str(window)

    def test_window_with_rows(self) -> None:
        window = Window(rows=(2, 4))
        assert window.rows == (2, 4)
        assert window.range is None
        assert "ROWS BETWEEN 2 FOLLOWING AND 4 FOLLOWING" in str(window)

    def test_window_range_unbounded_start(self) -> None:
        window = Window(range=(None, 1))
        assert "UNBOUNDED PRECEDING" in str(window)
        assert "1 FOLLOWING" in str(window)

    def test_window_range_unbounded_end(self) -> None:
        window = Window(range=(-4, None))
        assert "4 PRECEDING" in str(window)
        assert "UNBOUNDED FOLLOWING" in str(window)

    def test_window_rows_unbounded_start(self) -> None:
        window = Window(rows=(None, 2))
        assert "UNBOUNDED PRECEDING" in str(window)
        assert "2 FOLLOWING" in str(window)

    def test_window_rows_unbounded_end(self) -> None:
        window = Window(rows=(-4, None))
        assert "4 PRECEDING" in str(window)
        assert "UNBOUNDED FOLLOWING" in str(window)

    def test_window_current_row(self) -> None:
        window = Window(range=(0, 0))
        assert "CURRENT ROW AND CURRENT ROW" in str(window)

    def test_window_to_sql(self) -> None:
        window = Window(range=(-2, 0))
        sql = window.to_sql()
        assert sql.startswith("OVER (")
        assert sql.endswith(")")
        assert "RANGE BETWEEN 2 PRECEDING AND CURRENT ROW" in sql

    def test_window_to_sql_rows(self) -> None:
        window = Window(rows=(2, 4))
        sql = window.to_sql()
        assert "OVER (" in sql
        assert "ROWS BETWEEN 2 FOLLOWING AND 4 FOLLOWING" in sql

    def test_window_str_equals_to_sql(self) -> None:
        window = Window(range=(-2, 0))
        assert str(window) == window.to_sql()

    def test_window_preceding_with_negative_numbers(self) -> None:
        window = Window(range=(-5, -1))
        window_str = str(window)
        assert "5 PRECEDING" in window_str
        assert "1 PRECEDING" in window_str

    def test_window_following_with_positive_numbers(self) -> None:
        window = Window(range=(1, 5))
        window_str = str(window)
        assert "1 FOLLOWING" in window_str
        assert "5 FOLLOWING" in window_str

    def test_window_range_start_zero(self) -> None:
        window = Window(range=(0, 5))
        window_str = str(window)
        assert "CURRENT ROW" in window_str
        assert "5 FOLLOWING" in window_str

    def test_window_range_end_zero(self) -> None:
        window = Window(range=(-5, 0))
        window_str = str(window)
        assert "5 PRECEDING" in window_str
        assert "CURRENT ROW" in window_str

    def test_window_rows_start_zero(self) -> None:
        window = Window(rows=(0, 5))
        window_str = str(window)
        assert "CURRENT ROW" in window_str
        assert "5 FOLLOWING" in window_str

    def test_window_rows_end_zero(self) -> None:
        window = Window(rows=(-5, 0))
        window_str = str(window)
        assert "5 PRECEDING" in window_str
        assert "CURRENT ROW" in window_str

    def test_window_range_both_unbounded(self) -> None:
        window = Window(range=(None, None))
        window_str = str(window)
        assert "UNBOUNDED PRECEDING" in window_str
        assert "UNBOUNDED FOLLOWING" in window_str

    def test_window_rows_both_unbounded(self) -> None:
        window = Window(rows=(None, None))
        window_str = str(window)
        assert "UNBOUNDED PRECEDING" in window_str
        assert "UNBOUNDED FOLLOWING" in window_str
