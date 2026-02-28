import pytest
from pydantic.fields import FieldInfo

from pyclickhouse import Column


class TestColumn:
    def test_column_from_field(self) -> None:
        field = FieldInfo(annotation=str)
        column = Column.from_field("name", field)
        assert column._field == field
        assert column._name == "name"

    def test_column_defaults(self) -> None:
        with pytest.raises(TypeError):
            Column("String", default="one", alias="one")
            Column("String", default="one", materialized="one")
            Column("String", alias="one", materialized="one")

    def test_column_to_sql(self) -> None:
        # required
        with pytest.raises(TypeError):
            Column().to_sql()
            Column(type="String").to_sql()
            Column(name="name").to_sql()

        # base
        base = Column(name="name", type="String")
        assert base.to_sql() == "name String"

        # nullable
        nullable = Column(name="name", type="String", nullable=True)
        assert nullable.to_sql() == "name String NULL"
        not_nullable = Column(name="name", type="String", nullable=False)
        assert not_nullable.to_sql() == "name String NOT NULL"

        # default
        default = Column(name="name", type="String", default="one")
        assert default.to_sql() == "name String DEFAULT one"

        # materialized
        materialized = Column(name="name", type="String", materialized="one")
        assert materialized.to_sql() == "name String MATERIALIZED one"

        # alias
        alias = Column(name="name", type="String", alias="one")
        assert alias.to_sql() == "name String ALIAS one"

        # comment
        comment = Column(name="name", type="String", comment="one")
        assert comment.to_sql() == "name String COMMENT 'one'"

        # codec
        codec = Column(name="name", type="String", codec="LZ4")
        assert codec.to_sql() == "name String CODEC(LZ4)"

        # ttl
        ttl = Column(name="name", type="String", ttl="one")
        assert ttl.to_sql() == "name String TTL one"
