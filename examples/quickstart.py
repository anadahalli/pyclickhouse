from typing import Annotated

from pydantic import BaseModel

from pyclickhouse import Column, F, Query, Table, engines, get_client


async def main() -> None:
    client = get_client("clickhouse://localhost:9000/default")

    # model for table management and serialization
    class Event(BaseModel):
        name: Annotated[str, Column(type="String")]
        value: Annotated[int, Column(type="Int32")]

    # define tables
    table = Table(Event, engine=engines.MergeTree(order_by="name"))

    async with client:
        # create table
        await client.admin().create_table(table)

        # insert
        async with client.writer(table) as writer:
            await writer.insert(Event(name="first", value=1))
            await writer.insert(Event(name="second", value=2))

        # query
        query = Query(table).filter(table.name == "test_event")
        results = await client.reader(query, response_model=Event).query()

        for row in results:
            print(row)
        # Event(name="first", value=1)
        # Event(name="second", value=2)

        # aggregate
        query = Query(table).aggregate(res=F.sum(table.value))
        results = await client.reader(query).query()
        print(results)
        # [{"res": 3}]


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
