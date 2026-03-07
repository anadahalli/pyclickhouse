from typing import Annotated

import pytest
from pydantic import BaseModel
from pydantic.fields import FieldInfo

from pyclickhouse.fields import Column
from pyclickhouse.types import String


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

        column = Column(String(), "test")
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


class TestExpression:
    pass


class TestFunction:
    pass


class TestAggregate:
    pass
