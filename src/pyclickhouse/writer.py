from collections import deque
from typing import TYPE_CHECKING, Any, Self, Sequence

from clickhouse_connect.driver.insert import InsertContext
from pydantic import BaseModel

from pyclickhouse.table import Table

if TYPE_CHECKING:
    from pyclickhouse.client import Client


class Writer[T: BaseModel]:
    """Writer for inserting data into a ClickHouse table."""

    client: Client
    table: Table[T]
    model: type[T]
    context: InsertContext | None

    def __init__(
        self,
        client: Client,
        table: Table[T],
        *,
        batch: bool = True,
        batch_size: int = 1000,
        database: str | None = None,
        settings: dict[str, Any] | None = None,
        transport_settings: dict[str, str] | None = None,
    ) -> None:
        """
        Initializes a new Writer instance.

        Args:
            client: The ClickHouse client.
            table: The table to write to.
            batch: Whether to batch insert records. Defaults to True.
            batch_size: The number of records to insert in a batch. Defaults to 1000.
            database: The database to write to. Defaults to the database of the client.
            settings: The settings to use for the insert. Defaults to None.
            transport_settings: The transport settings to use for the insert. Defaults to None.
        """

        self.client = client
        self.table = table
        self.batch = batch
        self.batch_size = batch_size
        self.database = database
        self.settings = settings
        self.transport_settings = transport_settings

        self.context = None

        self.model = table.get_model()
        self.columns = [col.name for col in table.get_columns().values()]

        self._queue: deque[Sequence[Any]] = deque()
        self._written_rows: int = 0

    async def _create_context(self) -> InsertContext:
        table_name = self.table.get_name()
        table_columns = list(self.table.get_columns().values())
        column_names = [col.name for col in table_columns]
        column_type_names = [col.type for col in table_columns]

        context = await self.client.create_insert_context(
            table=table_name,
            database=self.database,
            column_names=column_names,
            column_type_names=column_type_names,
            column_oriented=False,
            settings=self.settings,
            transport_settings=self.transport_settings,
        )

        return context

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        await self.flush()

    @property
    def written_rows(self) -> int:
        """The number of rows written to the table."""
        return self._written_rows

    @property
    def queue_size(self) -> int:
        """The number of records in the queue."""
        return len(self._queue)

    def _serialize(self, data: T) -> Sequence[Any]:
        record = data.model_dump()
        return [record[col] for col in self.columns]

    def _get_next_batch(self) -> list[Sequence[Any]]:
        count = min(self.batch_size, len(self._queue))
        return [self._queue.popleft() for _ in range(count)]

    async def _insert_batch(self, data: Sequence[Sequence[Any]]) -> None:
        if self.context is None:
            self.context = await self._create_context()
        self.context.data = data
        summary = await self.client.data_insert(context=self.context)
        self._written_rows += summary.written_rows

    async def _flush_batch(self) -> None:
        batch = self._get_next_batch()
        await self._insert_batch(batch)

    async def flush(self) -> None:
        """Flushes the records in the queue to the table."""
        while self.queue_size:
            await self._flush_batch()

    async def insert(self, *items: T) -> None:
        """Inserts records into the table or queue them.

        If `batch` is `False`, the records are inserted immediately;
        otherwise, it is queued for batch insertion.

        Args:
            items: Records to insert.
        """
        if any(not isinstance(item, self.model) for item in items):
            raise TypeError(f"All items must be of type {str(self.model)}")

        data = [self._serialize(item) for item in items]

        if not self.batch:
            await self._insert_batch(data)
            return

        self._queue.extend(data)
        while self.queue_size >= self.batch_size:
            await self._flush_batch()
