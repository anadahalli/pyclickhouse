import pytest
from pydantic import BaseModel

from pyclickhouse import (
    Admin,
    Client,
    Column,
    Lifecycle,
    Query,
    Registry,
    Table,
    View,
)


@pytest.fixture
def admin(client: Client) -> Admin:
    return Admin(client)


class TestAdmin:
    # async def test_client(self, client: Client) -> None:
    #     admin = client.admin()
    #     assert isinstance(admin, Admin)
    #     assert admin.client is client

    async def test_database(self, admin: Admin) -> None:
        assert admin.client.database in await admin.show_databases()

        await admin.create_datbase("test_db")
        assert "test_db" in await admin.show_databases()

        await admin.drop_datbase("test_db")
        assert "test_db" not in await admin.show_databases()

    async def test_table(self, admin: Admin) -> None:
        assert await admin.show_tables() == []

        class Model(BaseModel):
            name: str
            value: int

        table = Table(Model, name="test", engine="Memory")
        await admin.create_table(table)
        assert await admin.show_tables() == ["test"]

        db_table = await admin.get_table("test")
        assert db_table.get_name() == table.get_name()
        assert db_table.get_engine() == table.get_engine()
        assert db_table.get_columns() == table.get_columns()

        await admin.drop_table(table)
        assert await admin.show_tables() == []

    async def test_column(self, admin: Admin) -> None:
        class Model(BaseModel):
            name: str

        table = Table(Model, name="model", engine="Memory")
        await admin.create_table(table)

        column = Column(type="Int32", name="value")
        await admin.add_column(table, column)
        db_table = await admin.get_table("model")
        assert db_table.get_columns() == {**table.get_columns(), "value": column}

        column = Column(type="String", name="value")
        await admin.modify_column(table, column)
        db_table = await admin.get_table("model")
        assert db_table.get_columns() == {**table.get_columns(), "value": column}

        await admin.drop_column(table, column)
        db_table = await admin.get_table("model")
        assert db_table.get_columns() == table.get_columns()

        await admin.drop_table(table)

    async def test_alter_table(self, admin: Admin) -> None:
        class Base(BaseModel):
            first: str
            second: str

        table = Table(Base, name="base", engine="Memory")
        await admin.create_table(table)

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

        await admin.drop_table(table)

    async def test_table_registry(self, admin: Admin) -> None:
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

        await admin.create_table(external)
        await admin.drop_all(registry)
        assert await admin.show_tables() == ["second", "third"]
        await admin.drop_table(protected, force=True)
        await admin.drop_table(external, force=True)

    async def test_view(self, admin: Admin) -> None:
        registry = Registry()

        assert await admin.show_views() == []

        View(
            name="basic_view",
            select="SELECT number FROM system.numbers LIMIT 100",
            registry=registry,
        )

        class Model(BaseModel):
            name: str
            value: int

        source = Table(
            Model,
            name="source_table",
            engine="Memory",
            registry=registry,
        )
        target = Table(
            Model,
            name="target_table",
            engine="Memory",
            registry=registry,
        )

        View(
            name="simple_view",
            select=Query(source),
            table=target,
            registry=registry,
        )

        await admin.create_all(registry)
        assert await admin.show_tables() == ["source_table", "target_table"]
        assert await admin.show_views() == ["basic_view", "simple_view"]

        # basic_sql = "SELECT * from basic_view LIMIT 6"
        # result = await admin.client.query(basic_sql)
        # assert result.values() == [0, 1, 2, 3, 4, 5]

        # data = [("one", 1), ("two", 2), ("three", 3), ("four", 4)]
        # assert await admin.client.insert(table=source.get_name(), data=data) == 8

        # result = await admin.client.query("SELECT * FROM target_table")
        # assert result.rows == data
