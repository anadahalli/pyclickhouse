from typing import TYPE_CHECKING, Any

from pydantic import BaseModel

from pyclickhouse.fields import Column
from pyclickhouse.query import Query
from pyclickhouse.registry import Registry, default_registry
from pyclickhouse.table import Table
from pyclickhouse.types import Lifecycle
from pyclickhouse.utils import comma_join, create_model_from_sql, logger
from pyclickhouse.view import View

if TYPE_CHECKING:
    from .client import Client


class AdminError(Exception):
    """Base exception for administrative errors."""

    pass


class Admin:
    """Provides administrative operations for the ClickHouse database.

    Args:
        client: The ClickHouse client to use for operations.
        database: The database to operate on.
        cluster: The cluster to operate on.
    """

    client: Client
    database: str
    cluster: str | None

    def __init__(
        self,
        client: Client,
        database: str | None = None,
        cluster: str | None = None,
    ) -> None:
        self.client = client
        self.database = database or client.database or "__default__"
        self.cluster = cluster

    # database
    async def show_databases(self) -> list[str]:
        """Show all databases"""
        query = "SHOW DATABASES"
        result = await self.client.query(query)
        return list(result.result_columns[0])

    async def create_datbase(
        self,
        name: str,
        *,
        if_not_exists: bool = True,
        cluster: str | None = None,
        engine: str | None = None,
        settings: dict[str, Any] | None = None,
        comment: str | None = None,
    ) -> None:
        """Create a new database."""
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
        await self.client.command(query)

    async def drop_datbase(
        self,
        name: str,
        *,
        if_exists: bool = True,
        cluster: str | None = None,
        sync: bool = False,
    ) -> None:
        """Drop a database."""
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
        await self.client.command(query)

    # table
    async def show_tables(self, *, database: str | None = None) -> list[str]:
        """Show all tables in the database."""
        parts: list[str] = []
        parts.append("SELECT name FROM system.tables")
        parts.append(f"WHERE database = '{database or self.database}'")
        parts.append("AND engine NOT IN ['View', 'MaterializedView']")
        parts.append("AND name NOT LIKE '.inner%'")
        query = " ".join(parts)
        result = await self.client.query(query)
        return list(result.result_columns[0]) if result.result_columns else []

    async def create_table(
        self,
        table: Table,
        *,
        if_not_exists: bool = True,
        database: str | None = None,
        cluster: str | None = None,
        engine: str | None = None,
    ) -> None:
        """Create a new table."""
        table_name = f"{database or self.database}.{table.get_name()}"
        parts: list[str] = []
        parts.append("CREATE TABLE")
        if if_not_exists:
            parts.append("IF NOT EXISTS")
        parts.append(table_name)
        if cluster or self.cluster:
            parts.append(f"ON CLUSTER {cluster or self.cluster}")
        columns = ", ".join([col.to_sql() for col in table.get_columns().values()])
        parts.append(f"({columns})")
        parts.append(f"ENGINE = {engine or table.get_engine()}")
        query = " ".join(parts)
        logger.debug(query)
        await self.client.command(query)

    async def drop_table(
        self,
        table: Table | str,
        *,
        if_exists: bool = True,
        if_empty: bool = False,
        database: str | None = None,
        cluster: str | None = None,
        sync: bool = False,
        force: bool = False,
    ) -> None:
        """Drop a table."""
        if isinstance(table, Table):
            if table.get_lifecycle() != Lifecycle.managed and not force:
                raise AdminError(f"Can not drop non managed table: {table.get_name()}")
            name = table.get_name()
        else:
            name = table

        table_name = f"{database or self.database}.{name}"
        parts: list[str] = []
        parts.append("DROP TABLE")
        if if_exists:
            parts.append("IF EXISTS")
        if if_empty:
            parts.append("IF EMPTY")
        parts.append(table_name)
        if cluster:
            parts.append(f"ON CLUSTER {cluster}")
        if sync:
            parts.append("SYNC")
        query = " ".join(parts)
        await self.client.command(query)

    async def get_table(
        self,
        name: str,
        *,
        database: str | None = None,
    ) -> Table:
        """Get a table by name."""
        database = database or self.database
        describe_query = f"DESC TABLE {database}.{name}"
        result = await self.client.query(describe_query)
        columns = list(result.named_results())
        engine_query = f"SELECT engine_full FROM system.tables WHERE database = '{database}' AND table = '{name}'"
        result = await self.client.command(engine_query)
        engine = str(result)
        return Table.from_sql(name=name, columns=columns, engine=engine)

    async def show_create_table(
        self,
        name: str,
        *,
        database: str | None = None,
    ) -> str:
        """Show the create table statement for a given table."""
        table_name = f"{database or self.database}.{name}"
        show_create = f"SHOW CREATE TABLE {table_name}"
        result = await self.client.command(show_create)
        return str(result)

    async def diff_table(
        self,
        table: Table,
        *,
        database: str | None = None,
    ) -> dict[str, list[Column]]:
        """Compare a local table with a table in the database and return the differences."""
        # table from the database
        db_table = await self.get_table(table.get_name(), database=database)

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
        drop_columns: bool = True,
        add_columns: bool = True,
        modify_columns: bool = True,
    ) -> None:
        """Alter a table by applying a set of operations."""
        if operations is None:
            operations = await self.diff_table(table)

        # Drop columns
        if drop_columns:
            for column in operations["drop_column"]:
                await self.drop_column(table, column, database=database)

        # Add columns
        if add_columns:
            for column in operations["add_column"]:
                await self.add_column(table, column, database=database)

        # Modify columns
        if modify_columns:
            for column in operations["modify_column"]:
                await self.modify_column(table, column, database=database)

    async def truncate_table(
        self,
        table: Table | str,
        *,
        database: str | None = None,
    ) -> None:
        """Truncate a table."""
        database = database or self.database
        table_name = table.get_name() if isinstance(table, Table) else table
        query = f"TRUNCATE TABLE {database}.{table_name}"
        await self.client.command(query)

    async def copy_table(
        self,
        table: Table,
        *,
        name: str,
        database: str | None = None,
    ) -> bool:
        """Copy a table to a new table."""
        raise NotImplementedError()

    # column
    async def add_column(
        self,
        table: Table,
        column: Column,
        *,
        database: str | None = None,
    ) -> None:
        """Add a column to a table."""
        table_name = f"{database or self.database}.{table.get_name()}"
        query = f"ALTER TABLE {table_name} ADD COLUMN {column.to_sql()}"
        await self.client.command(query)

    async def drop_column(
        self,
        table: Table,
        column: Column,
        *,
        database: str | None = None,
    ) -> None:
        """Drop a column from a table."""
        table_name = f"{database or self.database}.{table.get_name()}"
        query = f"ALTER TABLE {table_name} DROP COLUMN {column.name}"
        await self.client.command(query)

    async def modify_column(
        self,
        table: Table,
        column: Column,
        *,
        database: str | None = None,
    ) -> None:
        """Modify a column in a table."""
        table_name = f"{database or self.database}.{table.get_name()}"
        query = f"ALTER TABLE {table_name} DROP COLUMN {column.name}"
        query = f"ALTER TABLE {table_name} MODIFY COLUMN {column.to_sql()}"
        await self.client.command(query)

    # view
    async def show_views(self, *, database: str | None = None) -> list[str]:
        """Show all views in the database."""
        parts: list[str] = []
        parts.append("SELECT name FROM system.tables")
        parts.append(f"WHERE database = '{database or self.database}'")
        parts.append("AND engine IN ['View', 'MaterializedView']")
        query = " ".join(parts)
        result = await self.client.query(query)
        return list(result.result_columns[0]) if result.result_columns else []

    async def create_simple_view(
        self,
        view: View,
        *,
        replace: bool = True,
        database: str | None = None,
    ) -> None:
        """Create a new simple view."""
        view_name = f"{database or self.database}.{view.get_name()}"
        select_query = str(view.select)
        parts: list[str] = []
        parts.append("CREATE")
        if replace:
            parts.append("OR REPLACE")
        parts.append("VIEW")
        parts.append(view_name)
        parts.append("AS")
        parts.append(select_query)
        query = " ".join(parts)
        logger.debug(query)
        await self.client.command(query)

    async def create_materialized_view(
        self,
        view: View,
        table: Table,
        *,
        if_not_exists: bool = True,
        database: str | None = None,
    ) -> None:
        """Create a new materialized view."""
        view_name = f"{database or self.database}.{view.get_name()}"
        table_name = f"{database or self.database}.{table.get_name()}"
        select_query = str(view.select)
        parts: list[str] = []
        parts.append("CREATE MATERIALIZED VIEW")
        if if_not_exists:
            parts.append("IF NOT EXISTS")
        parts.append(view_name)
        parts.append(f"TO {table_name}")
        parts.append("AS")
        parts.append(select_query)
        query = " ".join(parts)
        logger.debug(query)
        await self.client.command(query)

    async def create_view(
        self,
        view: View,
        *,
        if_not_exists: bool = True,
        replace: bool = True,
        database: str | None = None,
    ) -> None:
        """Create a new view."""
        if view.table is not None:
            await self.create_materialized_view(
                view,
                table=view.table,
                if_not_exists=if_not_exists,
                database=database,
            )
        else:
            await self.create_simple_view(
                view,
                replace=replace,
                database=database,
            )

    async def drop_view(
        self,
        view: View | str,
        *,
        if_exists: bool = True,
        database: str | None = None,
        cluster: str | None = None,
        sync: bool = False,
        force: bool = False,
    ) -> None:
        """Drop a view."""
        if isinstance(view, View) and (
            view.get_lifecycle() != Lifecycle.managed and not force
        ):
            raise AdminError(f"Cannot drop non managed view: {view.get_name()}")

        name = view.get_name() if isinstance(view, View) else view
        view_name = f"{database or self.database}.{name}"
        parts: list[str] = []
        parts.append("DROP VIEW")
        if if_exists:
            parts.append("IF EXISTS")
        parts.append(view_name)
        if cluster:
            parts.append(f"ON CLUSTER {cluster}")
        if sync:
            parts.append("SYNC")
        query = " ".join(parts)
        await self.client.command(query)

    async def get_view(
        self,
        name: str,
        *,
        database: str | None = None,
    ) -> None:
        """Get a view by name."""
        raise NotImplementedError()

    # registry
    async def create_all(
        self,
        registry: Registry = default_registry,
        *,
        database: str | None = None,
        if_not_exists: bool = True,
    ) -> None:
        """Create all managed and protected tables and views from the registry.

        Args:
            registry: The registry to create tables and views from.
            database: The database to create tables and views in.
            if_not_exists: Whether to create tables and views if they already exist.
        """

        logger.info("Creating tables and views from registry...")

        for table in registry.list_tables():
            if table.get_lifecycle() != Lifecycle.external:
                logger.info("Creating Table({table})", table=table.get_name())
                await self.create_table(
                    table,
                    database=database,
                    if_not_exists=if_not_exists,
                )

        for view in registry.list_views():
            if table.get_lifecycle() != Lifecycle.external:
                logger.info("Creating View({view})", view=view.get_name())
                await self.create_view(
                    view,
                    database=database,
                    if_not_exists=if_not_exists,
                )

    async def drop_all(
        self,
        registry: Registry = default_registry,
        *,
        database: str | None = None,
        if_exists: bool = True,
    ) -> None:
        """Drop all managed tables and views from the registry.

        Args:
            registry: The registry to drop tables and views from.
            database: The database to drop tables and views from.
            if_exists: Whether to drop tables and views if they do not exist.
        """
        logger.info("Dropping tables and views from registry...")

        for table in registry.list_tables():
            if table.get_lifecycle() not in [Lifecycle.protected, Lifecycle.external]:
                logger.info("Dropping Table({table})", table=table.get_name())
                await self.drop_table(
                    table,
                    database=database,
                    if_exists=if_exists,
                )

        for view in registry.list_views():
            if table.get_lifecycle() not in [Lifecycle.protected, Lifecycle.external]:
                logger.info("Dropping View({view})", view=view.get_name())
                await self.drop_view(
                    view,
                    database=database,
                    if_exists=if_exists,
                )

    async def migrate_table(
        self,
        table: Table,
        *,
        database: str | None = None,
        force: bool = False,
    ) -> bool:
        """Migrate a table to the latest schema.

        Args:
            table: The table to migrate.
            database: The database to migrate the table to.
            force: Whether to force the migration even if the table is not managed.
        """
        should_migrate = False
        add_columns = True
        drop_columns = True
        modify_columns = True

        if table.get_lifecycle() == Lifecycle.external and force:
            should_migrate = True

        if table.get_lifecycle() == Lifecycle.protected:
            should_migrate = True
            if not force:
                drop_columns = False
                modify_columns = False

        if table.get_lifecycle() == Lifecycle.managed:
            should_migrate = True

        if should_migrate:
            logger.info("Migrating Table({table})", table=table.get_name())
            await self.alter_table(
                table,
                database=database,
                add_columns=add_columns,
                drop_columns=drop_columns,
                modify_columns=modify_columns,
            )
            return True

        return False

    async def migrate_view(
        self,
        view: View,
        *,
        database: str | None = None,
        force: bool = False,
    ) -> bool:
        """Migrate a view to the latest schema.

        Args:
            view: The view to migrate.
            database: The database to migrate the view to.
            force: Whether to force the migration even if the view is not managed.
        """
        raise NotImplementedError()

    async def migrate_all(
        self,
        registry: Registry = default_registry,
        *,
        database: str | None = None,
        create_all: bool = True,
        force: bool = False,
    ) -> None:
        """Migrate all managed tables and views from the registry.

        Args:
            registry: The registry to migrate tables and views from.
            database: The database to migrate tables and views to.
            force: Whether to force the migration even if the table or view is not managed.
        """
        if create_all:
            await self.create_all(registry, database=database)

        logger.info("Migrating tables and views from registry...")

        for table in registry.list_tables():
            await self.migrate_table(table, database=database, force=force)

        for view in registry.list_views():
            pass

    async def create_model(self, query: Query | str, name: str) -> type[BaseModel]:
        """Create a Pydantic model for the result of a given query"""
        query = query.compile() if isinstance(query, Query) else query
        describe_query = f"DESC (SELECT * FROM ({query}) LIMIT 0)"
        result = await self.client.query(describe_query)
        columns = list(result.named_results())
        return create_model_from_sql(name, columns)
