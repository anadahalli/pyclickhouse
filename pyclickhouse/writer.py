from collections import deque
from typing import TYPE_CHECKING, Any, Self, Sequence

from pydantic import BaseModel

from .table import Table

if TYPE_CHECKING:
    from .client import Client


class Writer:
    """Writer for inserting data into a ClickHouse table.

    If `batch` is `True`, the records are inserted immediately;
    otherwise, it is queued for batch insertion.

    Args:
        client: The ClickHouse client.
        table: The table to write to.
        batch: Whether to batch insert records.
        batch_size: The number of records to insert in a batch.
        database: The database to write to.
    """

    _client: Client
    _table: Table

    def __init__(
        self,
        client: Client,
        table: Table,
        *,
        batch: bool = True,
        batch_size: int = 1000,
        database: str | None = None,
    ) -> None:
        self._client = client
        self._table = table
        self._batch = batch
        self._batch_size = batch_size
        self._database = database

        self._table_name = table.get_name()
        self._table_model = table.get_model()
        self._table_columns = list(table.get_columns().keys())

        self._records: deque[BaseModel] = deque()
        self._count: int = 0

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.flush()

    @property
    def written_rows(self) -> int:
        """The number of rows written to the table."""
        return self._count

    @property
    def queue_length(self) -> int:
        """The number of records in the queue."""
        return len(self._records)

    def _serialize(self, data: BaseModel) -> Sequence[Any]:
        return tuple(data.model_dump().values())

    def _get_next_batch(self) -> list[BaseModel]:
        count = min(self._batch_size, len(self._records))
        return [self._records.pop() for _ in range(count)]

    async def _insert(self, data: Sequence[Sequence[Any]]) -> None:
        count = await self._client.insert(
            table=self._table_name,
            data=data,
            columns=self._table_columns,
            database=self._database or self._client.database,
        )
        self._count += count

    async def flush(self) -> None:
        """Flushes the records in the queue to the table."""
        while len(self._records):
            items = self._get_next_batch()
            data = [self._serialize(item) for item in items]
            # print("writer", data)
            await self._insert(data)

    async def insert(self, *items: BaseModel) -> None:
        """Inserts records into the table or queue them.

        If `batch` is `True`, the record is inserted immediately;
        otherwise, it is queued for batch insertion.

        Args:
            items: Records to insert.
        """
        for item in items:
            if not isinstance(item, self._table_model):
                raise TypeError(
                    f"Expected {str(self._table_model)}, got {str(type(item))}"
                )

            self._records.append(item)

        if not self._batch:
            await self.flush()
