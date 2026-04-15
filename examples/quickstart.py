from typing import Annotated

from pydantic import BaseModel

import pyclickhouse as ch


async def main() -> None:
    client = ch.create_async_client(dsn="clickhouse://localhost:9000/default")

    # model for table management and serialization
    class Event(BaseModel):
        name: Annotated[str, ch.Column(type="String")]
        value: Annotated[int, ch.Column(type="Int32")]

    # define tables
    table = ch.Table(Event, engine=ch.engines.MergeTree(order_by="name"))

    async with client:
        # create table
        admin = ch.Admin(client)
        await admin.create_table(table)

        # insert
        writer = ch.Writer(client, table)
        async with writer:
            await writer.insert(Event(name="first", value=1))
            await writer.insert(Event(name="second", value=2))

        # build query
        query = ch.Query(table).filter(table.name == "test_event")

        # read
        reader = ch.Reader(client, query, model=Event)
        results = reader.query()

        async for row in results:
            print(row)
        # Event(name="first", value=1)
        # Event(name="second", value=2)

        # aggregate
        query = ch.Query(table).aggregate(res=F.sum(table.value))
        reader = ch.Reader(client, query)
        results = reader.query()
        print(results)
        # [{"res": 3}]


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
