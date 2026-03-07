from typing import Annotated

from pydantic import BaseModel

from pyclickhouse.engines import Memory, MergeTree
from pyclickhouse.fields import Column
from pyclickhouse.table import Table, table


class TestTable:
    def test_table_from_model(self) -> None:
        class Model(BaseModel):
            name: str
            value: int

        model = Table.from_model(Model)
        assert isinstance(model, Table)
        assert model._model == Model
        assert model._columns == {
            "name": Column(name="name", type="String"),
            "value": Column(name="value", type="Int32"),
        }
        assert model._name == "model"
        assert model._engine == MergeTree()

        model = Table.from_model(Model, name="test", engine=Memory())
        assert model._name == "test"
        assert model._engine == Memory()

        class ModelColumn(BaseModel):
            name: Annotated[str, Column(name="new_name")]
            value: Annotated[int, Column(type="Int8")]

        model = Table.from_model(ModelColumn)
        assert model._columns == {
            "name": Column(name="new_name", type="String"),
            "value": Column(name="value", type="Int8"),
        }

    def test_table_from_sql(self) -> None:
        columns_sql = [
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
        engine_sql = "MergeTree ORDER BY key SETTINGS index_granularity = 8192"

        model = Table.from_sql(
            name="model",
            engine_sql=engine_sql,
            columns_sql=columns_sql,
        )
        assert model._name == "model"
        assert model._engine == engine_sql
        assert model._columns == {
            "key": Column(name="key", type="String"),
            "val": Column(name="val", type="Int32"),
        }

    def test_table_to_sql(self) -> None:
        class Model(BaseModel):
            key: str
            val: int

        model = table(Model)
        create_sql = "model (key String, val Int32) ENGINE = MergeTree ORDER BY tuple()"
        assert model.to_create_sql() == create_sql
        insert_sql = "model (key, val) VALUES"
        assert model.to_insert_sql() == insert_sql
