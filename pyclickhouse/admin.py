from typing import Any

from .client import Client
from .fields import Column
from .table import Table
from .utils import comma_join


class Admin:
    def __init__(
        self,
        client: Client,
        database: str,
        cluster: str | None = None,
    ) -> None:
        self.client = client
        self.database = database
        self.cluster = cluster

    # database
    async def show_databases(self) -> list[str]:
        query = "SHOW DATABASES"
        print(query)
        return []

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
        print(query)
        return True

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
        print(query)
        return True

    # table
    async def show_tables(self) -> list[str]:
        query = f"SHOW TABLES FROM {self.database}"
        result = await self.client.command(query)
        return [res["name"] for res in await result.fetchall()]

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
        print(query)
        return True

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
        print(query)
        return True

    async def alter_table(
        self,
        table: Table,
        *,
        database: str | None = None,
    ) -> bool:
        # to_drop: list[Column] = []
        to_add: list[Column] = []
        to_modify: list[Column] = []
        db_table = await self.get_table(table._name)

        to_drop = set(db_table._columns.values()) - set(table._columns.values())

        # Drop columns
        for column in to_drop:
            await self.drop_column(column, table)
        # Add columns
        for column in to_add:
            await self.add_column(column, table)
        # Modify columns
        for column in to_modify:
            await self.modify_column(column, table)

        return True

    async def get_table(
        self,
        name: str,
        *,
        database: str | None = None,
    ) -> Table:
        result = await self.execute(f"DESC TABLE {self.database}.{name}")
        columns = await result.fetchall()
        query = f"SELECT engine_full FROM system.tables WHERE database = '{self.database}' AND table = '{name}'"
        result = await self.execute(query)
        engine_full = await result.fetchone()
        engine = engine_full.get("engine_full", "")
        return Table.from_sql(name=name, engine_sql=engine, columns_sql=columns)

    # column
    async def add_column(
        self,
        column: Column,
        table: Table,
    ) -> bool:
        query = f"ALTER TABLE {table._name} ADD COLUMN {column.to_sql()}"
        result = await self.execute(query)
        return bool(result.rowcount)

    async def drop_column(
        self,
        column: Column,
        table: Table,
    ) -> bool:
        query = f"ALTER TABLE {table._name} DROP COLUMN {column.name}"
        result = await self.execute(query)
        return bool(result.rowcount)

    async def modify_column(
        self,
        column: Column,
        table: Table,
    ) -> bool:
        query = f"ALTER TABLE {table._name} MODIFY COLUMN {column.to_sql()}"
        result = await self.execute(query)
        return bool(result.rowcount)

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
    async def create_registry(self, registry) -> None:
        pass

    async def drop_registry(self, registry) -> None:
        pass
