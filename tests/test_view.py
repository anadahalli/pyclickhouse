from datetime import date, datetime
from typing import Annotated

from pydantic import BaseModel

from pyclickhouse import Aggregate, Client, Column, F, Query, Registry, Table, View
from pyclickhouse.admin import Admin
from pyclickhouse.engines import AggregatingMergeTree, MergeTree
from pyclickhouse.writer import Writer


class TestView:
    async def test_view_full(self, client: Client) -> None:
        registry = Registry()

        class Hourly(BaseModel):
            domain_name: Annotated[str, Column(type="String")]
            event_time: Annotated[datetime, Column(type="DateTime")]
            count_views: Annotated[int, Column(type="UInt64")]

        hourly = Table(
            Hourly,
            name="hourly_data",
            engine=MergeTree(order_by="domain_name"),
            registry=registry,
        )

        class Monthly(BaseModel):
            domain_name: Annotated[str, Column(type="String")]
            month: Annotated[date, Column(type="Date")]
            sum_count_views: Annotated[
                int, Column(type="AggregateFunction(sum, UInt64)")
            ]

        monthly = Table(
            Monthly,
            name="monthly_data",
            engine=AggregatingMergeTree(order_by="(domain_name, month)"),
            registry=registry,
        )

        select_query = Query(hourly).group(
            domain_name=hourly.domain_name,
            month=F.toDate(F.toStartOfMonth(hourly.event_time)),
            sum_count_views=Aggregate(F.sumState(hourly.count_views)),
        )

        view = View(
            name="monthly_aggregated_mv",
            select=select_query,
            table=monthly,
            registry=registry,
        )
        assert view.get_name() == "monthly_aggregated_mv"

        await Admin(client).create_all(registry)

        data = [
            Hourly(
                domain_name="clickhouse.com",
                event_time=datetime(2020, 3, 2),
                count_views=1,
            ),
            Hourly(
                domain_name="clickhouse.com",
                event_time=datetime(2020, 3, 5),
                count_views=2,
            ),
            Hourly(
                domain_name="clickhouse.com",
                event_time=datetime(2021, 6, 8),
                count_views=3,
            ),
            Hourly(
                domain_name="clickhouse.com",
                event_time=datetime(2021, 6, 10),
                count_views=6,
            ),
        ]

        writer = Writer(client=client, table=hourly, batch=False)
        await writer.insert(*data)
        assert writer.written_rows == 4

        query = Query(monthly).group(
            domain_name=monthly.domain_name,
            month=monthly.month,
            sum_count_views=Aggregate(F.sumMerge(monthly.sum_count_views)),
        )

        result = await client.query(str(query))
        items = list(result.named_results())
        assert len(items) == 2
        assert items[0]["sum_count_views"] == 3
        assert items[1]["sum_count_views"] == 9
