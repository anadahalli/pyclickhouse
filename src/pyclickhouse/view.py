from pyclickhouse.query import Query
from pyclickhouse.registry import Registry, default_registry
from pyclickhouse.table import Table
from pyclickhouse.types import Lifecycle


class View:
    """
    A simple view or a materialized view in ClickHouse.

    Args:
        name: The name of the view.
        select: The query to select rows from the table.
        table: The table to materialize or None for a simple view.
        lifecycle: The lifecycle of the view. Defaults to Lifecycle.managed.
        registry: The registry to register the view with. Defaults to the global registry.
    """

    name: str
    select: Query | str
    table: Table | None

    def __init__(
        self,
        name: str,
        select: Query | str,
        *,
        table: Table | None = None,
        lifecycle: Lifecycle = Lifecycle.managed,
        registry: Registry = default_registry,
    ) -> None:
        self.name = name
        self.select = select
        self.table = table
        self._lifecycle = lifecycle
        self._registry = registry
        registry.register_view(self)

    def __str__(self) -> str:
        return self.get_name()

    @property
    def is_materialized(self) -> bool:
        """Return True if the view is materialized, False otherwise."""
        return self.table is not None

    def get_name(self) -> str:
        """Return the name of the view."""
        return self.name

    def get_lifecycle(self) -> Lifecycle:
        """Return the lifecycle of the view."""
        return self._lifecycle
