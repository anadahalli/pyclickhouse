from typing import Annotated

import pytest

from pyclickhouse import Column, Expression, MergeTree, Table, TableConfig


class TestTable:
    def test_table_initialize(self) -> None:
        class Model(Table):
            table_config = TableConfig(
                engine=MergeTree(order_by="value"),
                name="test_table",
            )

            name: Annotated[str, Column(type="String", name="name")]
            value: Annotated[int, Column(type="UInt32", name="value")]

        assert Model.table_config.name == "test_table"
        assert Model.table_config.engine == MergeTree(order_by="value")
        columns = {
            "name": Column(
                type="String",
                name="name",
                nullable=None,
                default=None,
                materialized=None,
                alias=None,
                codec=None,
                ttl=None,
                comment=None,
            ),
            "value": Column(
                type="UInt32",
                name="value",
                nullable=None,
                default=None,
                materialized=None,
                alias=None,
                codec=None,
                ttl=None,
                comment=None,
            ),
        }
        assert Model.table_columns == columns

    def test_table_to_create_sql(self) -> None:
        class Model(Table):
            name: Annotated[str, Column(type="String")]
            value: int

        sql = "CREATE TABLE IF NOT EXISTS model (name String, value Int32) ENGINE = MergeTree() ORDER BY tuple()"
        assert Model.to_create_sql() == sql

    def test_table_to_insert_sql(self) -> None:
        class Model(Table):
            name: Annotated[str, Column(type="String")]
            value: int

        sql = "INSERT INTO model (name, value) VALUES"
        model = Model(name="test", value=1)
        assert model.to_insert_sql() == sql

    def test_table_column_access(self) -> None:
        class Model(Table):
            name: Annotated[str, Column(type="String")]
            value: int

        with pytest.raises(AttributeError):
            Model.unknown  # type: ignore

        assert isinstance(Model.name, Expression)
        assert isinstance(Model.value, Expression)
