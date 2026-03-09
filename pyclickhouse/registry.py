from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .table import Table


class Registry:
    tables: dict[str, Table]

    def __init__(self) -> None:
        self._tables: dict[str, Table] = {}

    def register_table(self, table: Table) -> None:
        self._tables[table._name] = table

    def unregister_table(self, name: str) -> None:
        self._tables.pop(name, None)

    def get_table(self, name: str) -> Table | None:
        return self._tables.get(name)


registry = Registry()
