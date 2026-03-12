from .query import Query
from .registry import Registry, registry
from .table import Table
from .types import Lifecycle


class View:
    """
    A view or a materialized view in ClickHouse.

    Args:
        name: The name of the view.
        select: The query to select rows from the table.
        table: The table to materialize or None for a simple view.
    """

    def __init__(
        self,
        name: str,
        select: Query | str,
        *,
        table: Table | None = None,
        lifecycle: Lifecycle = Lifecycle.managed,
        registry: Registry = registry,
    ) -> None:
        self.name = name
        self.select = select
        self.table = table
        self._lifecycle = lifecycle
        self._registry = registry
        registry.register_view(self)

    @property
    def is_materialized(self) -> bool:
        return self.table is not None

    def get_name(self) -> str:
        return self.name

    def get_lifecycle(self) -> Lifecycle:
        return self._lifecycle
