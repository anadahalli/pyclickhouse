from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .table import Table


class Registry:
    def __init__(self):
        self.tables: dict[str, type[Table]] = {}

    def register_table(self, table: type[Table]):
        self.tables[table.get_table_name()] = table

    def get_table(self, name: str) -> type[Table] | None:
        return self.tables.get(name)


default_registry = Registry()
