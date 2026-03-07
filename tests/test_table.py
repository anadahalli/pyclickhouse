from typing import Annotated, ClassVar

from pydantic import BaseModel

from pyclickhouse.engines import MergeTree
from pyclickhouse.fields import Column
from pyclickhouse.table import Table, TableConfig


class TestTable:
    def test_table_from_model(self) -> None:
        class Model(BaseModel):
            key: str
            val: int

        table = Table.from_model(Model)
        assert isinstance(table, Table)
        assert table._table_model == Model
        assert table._table_name == "model"
        assert table._table_config == TableConfig()
        assert table._table_columns == {
            "key": Column(name="key", type="String"),
            "val": Column(name="val", type="Int32"),
        }

        class ModelConfig(BaseModel):
            table_config: ClassVar = TableConfig(
                engine=MergeTree(),
                order_by="name",
            )
            name: str

        table = Table.from_model(ModelConfig)
        assert isinstance(table, Table)
        assert table._table_model == ModelConfig
        assert table._table_name == "model_config"
        assert table._table_config == TableConfig(
            engine=MergeTree(),
            order_by="name",
        )
        assert table._table_columns == {
            "name": Column(name="name", type="String"),
        }

        class ModelColumns(BaseModel):
            name: Annotated[str, Column(name="new_name")]
            value: Annotated[int, Column(type="Int8")]

        table = Table.from_model(ModelColumns)
        assert isinstance(table, Table)
        assert table._table_model == ModelColumns
        assert table._table_name == "model_columns"
        assert table._table_config == TableConfig()
        assert table._table_columns == {
            "name": Column(name="new_name", type="String"),
            "value": Column(name="value", type="Int8"),
        }

    def test_table_from_database(self) -> None:
        columns = [
            {
                "name": "key",
                "type": "String",
                "default_type": "",
                "default_expression": "",
                "comment": "",
                "codec_expression": "",
                "ttl_expression": "",
            },
            {
                "name": "val",
                "type": "Int32",
                "default_type": "",
                "default_expression": "",
                "comment": "",
                "codec_expression": "",
                "ttl_expression": "",
            },
        ]
        engine_full = "MergeTree ORDER BY key SETTINGS index_granularity = 8192"

        table = Table.from_database(name="model", engine=engine_full, columns=columns)
        assert table._table_name == "model"
        assert table._table_config == TableConfig(
            engine="MergeTree",
            order_by="key",
            settings={"index_granularity": "8192"},
        )
        assert table._table_columns == {
            "key": Column(name="key", type="String"),
            "val": Column(name="val", type="Int32"),
        }

    def test_table_to_sql(self) -> None:
        class Model(BaseModel):
            key: str
            val: int

        table = Table.from_model(Model)
        create_sql = "CREATE TABLE IF NOT EXISTS model (key String, val Int32) ENGINE = MergeTree ORDER BY tuple()"
        assert table.to_create_sql() == create_sql
        drop_sql = "DROP TABLE IF EXISTS model"
        assert table.to_drop_sql() == drop_sql
        insert_sql = "INSERT INTO model (key, val) VALUES"
        assert table.to_insert_sql() == insert_sql
