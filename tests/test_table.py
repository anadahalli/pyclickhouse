from typing import Annotated

from pydantic import BaseModel

from pyclickhouse.engines import Memory, MergeTree
from pyclickhouse.fields import Column
from pyclickhouse.table import Table


class TestTable:
    def test_table(self) -> None:
        class Model(BaseModel):
            name: str
            value: int

        model = Table(Model)
        assert isinstance(model, Table)
        assert model._model == Model
        assert model._columns == {
            "name": Column(name="name", type="String"),
            "value": Column(name="value", type="Int32"),
        }
        assert model._name == "model"
        assert model._engine == MergeTree()

        model = Table(Model, name="test", engine=Memory())
        assert model._name == "test"
        assert model._engine == Memory()

        class ModelColumn(BaseModel):
            name: Annotated[str, Column(name="new_name")]
            value: Annotated[int, Column(type="Int8")]

        model = Table(ModelColumn)
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
            columns=columns_sql,
            engine=engine_sql,
        )
        assert model._name == "model"
        assert model._engine == engine_sql
        assert model._columns == {
            "key": Column(name="key", type="String"),
            "val": Column(name="val", type="Int32"),
        }

    def test_table_registry(self) -> None:
        pass
