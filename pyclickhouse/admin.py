from typing import TYPE_CHECKING, Any

from .fields import Column
from .registry import Registry, registry
from .table import Table
from .types import Lifecycle
from .utils import comma_join

if TYPE_CHECKING:
    from .client import Client


class Admin:
    client: Client

    def __init__(
        self,
        client: Client,
        database: str | None = None,
        cluster: str | None = None,
    ) -> None:
        self.client = client
        self.database = database
        self.cluster = cluster

    # database
    async def show_databases(self) -> list[str]:
        query = "SHOW DATABASES"
        result = await self.client.query(query)
        return result.values()

    async def create_datbase(
        self,
        name: str,
        *,
        if_not_exists: bool = True,
        cluster: str | None = None,
        engine: str | None = None,
        settings: dict[str, Any] | None = None,
        comment: str | None = None,
    ) -> bool:
        parts: list[str] = []
        parts.append("CREATE DATABASE")
        if if_not_exists:
            parts.append("IF NOT EXISTS")
        parts.append(name)
        if cluster or self.cluster:
            parts.append(f"ON CLUSTER {cluster or self.cluster}")
        if engine:
            parts.append(f"ENGINE = {engine}")
        if settings:
            parts.append(comma_join(settings, prefix="SETTINGS"))
        if comment:
            parts.append(f"COMMENT {comment}")
        query = " ".join(parts)
        return await self.client.command(query)

    async def drop_datbase(
        self,
        name: str,
        *,
        if_exists: bool = True,
        cluster: str | None = None,
        sync: bool = False,
    ) -> bool:
        parts: list[str] = []
        parts.append("DROP DATABASE")
        if if_exists:
            parts.append("IF EXISTS")
        parts.append(name)
        if cluster or self.cluster:
            parts.append(f"ON CLUSTER {cluster or self.cluster}")
        if sync:
            parts.append("SYNC")
        query = " ".join(parts)
        return await self.client.command(query)

    # table
    async def show_tables(self) -> list[str]:
        query = f"SHOW TABLES FROM {self.database}"
        result = await self.client.query(query)
        return result.values()

    async def create_table(
        self,
        table: Table,
        *,
        if_not_exists: bool = True,
        database: str | None = None,
        cluster: str | None = None,
        engine: str | None = None,
    ) -> bool:
        parts: list[str] = []
        parts.append("CREATE TABLE")
        if if_not_exists:
            parts.append("IF NOT EXISTS")
        parts.append(f"{database or self.database}.{table.get_name()}")
        if cluster or self.cluster:
            parts.append(f"ON CLUSTER {cluster or self.cluster}")
        columns = ", ".join([col.to_sql() for col in table.get_columns().values()])
        parts.append(f"({columns})")
        parts.append(f"ENGINE = {engine or table.get_engine()}")
        query = " ".join(parts)
        return await self.client.command(query)

    async def drop_table(
        self,
        table: Table | str,
        *,
        if_exists: bool = True,
        if_empty: bool = False,
        database: str | None = None,
        cluster: str | None = None,
        sync: bool = False,
    ) -> bool:
        if isinstance(table, Table):
            if table.get_lifecycle() in [Lifecycle.protected, Lifecycle.external]:
                print(f"Table({table.get_name()}) is not managed")
                return False

        parts: list[str] = []
        parts.append("DROP TABLE")
        if if_exists:
            parts.append("IF EXISTS")
        if if_empty:
            parts.append("IF EMPTY")
        name = table.get_name() if isinstance(table, Table) else table
        parts.append(f"{database or self.database}.{name}")
        if cluster:
            parts.append(f"ON CLUSTER {cluster}")
        if sync:
            parts.append("SYNC")
        query = " ".join(parts)
        return await self.client.command(query)

    async def get_table(
        self,
        name: str,
        *,
        database: str | None = None,
    ) -> Table:
        database = database or self.database
        describe_query = f"DESC TABLE {database}.{name}"
        engine_query = f"SELECT engine_full FROM system.tables WHERE database = '{database}' AND table = '{name}'"
        result = await self.client.query(describe_query)
        columns = result.items()
        result = await self.client.query(engine_query)
        engine = result.values()[0]
        return Table.from_sql(name=name, columns=columns, engine=engine)

    async def show_create_table(
        self,
        name: str,
        *,
        database: str | None = None,
    ) -> str:
        show_create = f"SHOW CREATE TABLE {database or self.database}.{name}"
        result = await self.client.query(show_create)
        return result.values()[0]

    async def diff_table(
        self,
        table: Table,
        *,
        database: str | None = None,
    ) -> dict[str, list[Column]]:
        # table from the database
        db_table = await self.get_table(table.get_name())

        # columns
        local = table.get_columns().values()
        remote = db_table.get_columns().values()

        # column names
        local_names = set(col.name for col in local)
        remote_names = set(col.name for col in remote)

        # find changes to local table
        operations = {
            "drop_column": [],
            "add_column": [],
            "modify_column": [],
        }

        # Drop columns
        for name in remote_names - local_names:
            for column in [col for col in remote if col.name == name]:
                operations["drop_column"].append(column)

        # Add columns
        for name in local_names - remote_names:
            for column in [col for col in local if col.name == name]:
                operations["add_column"].append(column)

        # Modify columns
        for this, that in zip(local, remote):
            if this != that:
                operations["modify_column"].append(this)

        return operations

    async def alter_table(
        self,
        table: Table,
        operations: dict[str, list[Column]] | None = None,
        *,
        database: str | None = None,
    ) -> bool:
        if operations is None:
            operations = await self.diff_table(table)

        # Drop columns
        for column in operations["drop_column"]:
            await self.drop_column(table, column)

        # Add columns
        for column in operations["add_column"]:
            await self.add_column(table, column)

        # Modify columns
        for column in operations["modify_column"]:
            await self.modify_column(table, column)

        return True

    async def copy_table(
        self,
        table: Table,
        *,
        name: str,
        database: str | None = None,
    ) -> bool:
        raise NotImplementedError()

    # column
    async def add_column(
        self,
        table: Table,
        column: Column,
    ) -> bool:
        query = f"ALTER TABLE {table.get_name()} ADD COLUMN {column.to_sql()}"
        return await self.client.command(query)

    async def drop_column(
        self,
        table: Table,
        column: Column,
    ) -> bool:
        query = f"ALTER TABLE {table.get_name()} DROP COLUMN {column.name}"
        return await self.client.command(query)

    async def modify_column(
        self,
        table: Table,
        column: Column,
    ) -> bool:
        query = f"ALTER TABLE {table.get_name()} MODIFY COLUMN {column.to_sql()}"
        return await self.client.command(query)

    # view
    async def show_views(self) -> None:
        pass

    async def create_view(self) -> None:
        pass

    async def drop_view(self) -> None:
        pass

    async def get_view(self) -> None:
        pass

    # registry
    async def create_all(self, registry: Registry = registry) -> None:
        for table in registry.list_tables():
            if table.get_lifecycle() != Lifecycle.external:
                print(f"Create Table({table.get_name()})")
                await self.create_table(table)

    async def drop_all(self, registry: Registry = registry) -> None:
        for table in registry.list_tables():
            if table.get_lifecycle() not in [Lifecycle.protected, Lifecycle.external]:
                print(f"Drop Table({table.get_name()})")
                await self.drop_table(table)
