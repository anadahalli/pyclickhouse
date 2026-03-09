import pytest
from pydantic import BaseModel

from pyclickhouse.admin import Admin
from pyclickhouse.client import HttpClient
from pyclickhouse.fields import Column
from pyclickhouse.registry import Registry
from pyclickhouse.table import Table
from pyclickhouse.types import Lifecycle


@pytest.fixture
def admin(http_client: HttpClient) -> Admin:
    return http_client.admin()


class TestAdmin:
    async def test_database(self, admin: Admin) -> None:
        assert admin.client.database in await admin.show_databases()

        assert await admin.create_datbase("test_db")
        assert "test_db" in await admin.show_databases()

        assert await admin.drop_datbase("test_db")
        assert "test_db" not in await admin.show_databases()

    async def test_table(self, admin: Admin) -> None:
        assert await admin.show_tables() == []

        class Model(BaseModel):
            name: str
            value: int

        table = Table(Model, name="test", engine="Memory")
        assert await admin.create_table(table)
        assert await admin.show_tables() == ["test"]

        db_table = await admin.get_table("test")
        assert db_table.get_name() == table.get_name()
        assert db_table.get_engine() == table.get_engine()
        assert db_table.get_columns() == table.get_columns()

        assert await admin.drop_table(table)
        assert await admin.show_tables() == []

    async def test_column(self, admin: Admin) -> None:
        class Model(BaseModel):
            name: str

        table = Table(Model, name="model", engine="Memory")
        assert await admin.create_table(table)

        column = Column(type="Int32", name="value")
        assert await admin.add_column(table, column)
        db_table = await admin.get_table("model")
        assert db_table.get_columns() == {**table.get_columns(), "value": column}

        column = Column(type="String", name="value")
        assert await admin.modify_column(table, column)
        db_table = await admin.get_table("model")
        assert db_table.get_columns() == {**table.get_columns(), "value": column}

        assert await admin.drop_column(table, column)
        db_table = await admin.get_table("model")
        assert db_table.get_columns() == table.get_columns()

        assert await admin.drop_table(table)

    async def test_alter_table(self, admin: Admin) -> None:
        class Base(BaseModel):
            first: str
            second: str

        table = Table(Base, name="base", engine="Memory")
        assert await admin.create_table(table)

        # drop column
        class BaseDrop(BaseModel):
            first: str

        table = Table(BaseDrop, name="base", engine="Memory")
        await admin.alter_table(table)
        db_table = await admin.get_table("base")
        assert db_table.get_columns() == table.get_columns()

        # add column
        class BaseAdd(BaseModel):
            first: str
            third: str

        table = Table(BaseAdd, name="base", engine="Memory")
        await admin.alter_table(table)
        db_table = await admin.get_table("base")
        assert db_table.get_columns() == table.get_columns()

        # modify column
        class BaseModify(BaseModel):
            first: str
            third: int

        table = Table(BaseModify, name="base", engine="Memory")
        await admin.alter_table(table)
        db_table = await admin.get_table("base")
        assert db_table.get_columns() == table.get_columns()

        assert await admin.drop_table(table)

    async def test_view(self, admin: Admin) -> None:
        pass

    async def test_registry(self, admin: Admin) -> None:
        registry = Registry()

        class First(BaseModel):
            name: str

        managed = Table(First, registry=registry, lifecycle=Lifecycle.managed)

        class Second(BaseModel):
            value: int

        protected = Table(Second, registry=registry, lifecycle=Lifecycle.protected)

        class Third(BaseModel):
            val: float

        external = Table(Third, registry=registry, lifecycle=Lifecycle.external)

        assert registry.list_tables() == [managed, protected, external]
        await admin.create_all(registry)
        assert await admin.show_tables() == ["first", "second"]

        assert await admin.create_table(external)
        await admin.drop_all(registry)
        assert await admin.show_tables() == ["second", "third"]
