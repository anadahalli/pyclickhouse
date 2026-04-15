from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyclickhouse.table import Table
    from pyclickhouse.view import View


class Registry:
    """A registry for tables and views."""

    _tables: dict[str, Table]
    _views: dict[str, View]

    def __init__(self) -> None:
        self._tables: dict[str, Table] = {}
        self._views: dict[str, View] = {}

    def register_table(self, table: Table) -> None:
        self._tables[table._name] = table

    def unregister_table(self, name: str) -> None:
        self._tables.pop(name, None)

    def get_table(self, name: str) -> Table | None:
        return self._tables.get(name)

    def list_tables(self) -> list[Table]:
        return list(self._tables.values())

    def register_view(self, view: View) -> None:
        self._views[view.name] = view

    def unregister_view(self, name: str) -> None:
        self._views.pop(name, None)

    def get_view(self, name: str) -> View | None:
        return self._views.get(name)

    def list_views(self) -> list[View]:
        return list(self._views.values())

    def clear(self) -> None:
        self._tables.clear()
        self._views.clear()


# default global registry
default_registry = Registry()
