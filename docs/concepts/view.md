---
title: View
---

A `View` in ClickHouse is a virtual table that executes a query on-demand (simple view) or stores materialized results in a backing table (materialized view). PyClickHouse's `View` class simplifies creating and managing both types.

---

## Simple Views

Simple views are virtual tables that execute a stored query each time they're accessed. They don't store data—they're just named queries.

### Creating a Simple View

Create a simple view using a `Query` or SQL string:

```py
from pyclickhouse import View, Table, Query
from pydantic import BaseModel

class Event(BaseModel):
    user_id: int
    event_name: str
    value: float

events = Table(model=Event)

# Create a simple view from a query
high_value_events = View(
    name="high_value_events",
    select=Query(events).filter(events.value > 100)
)

# Or use a raw SQL string
another_view = View(
    name="active_users",
    select="SELECT DISTINCT user_id FROM events WHERE value > 50"
)
```

### Simple View Characteristics

- **No storage**: Results are computed on-demand each time you query the view
- **Always current**: Reflects the latest data in the underlying table
- **Lower overhead**: No extra storage or synchronization needed
- **Slower queries**: Recomputes the query every time you access it

### Querying Simple Views

Query a simple view by passing a SQL string or Query to Reader:

```py
from pyclickhouse import Client, Reader, Query

async def query_simple_view():
    client = Client()
    
    async with client:
        # Query using raw SQL string
        reader = Reader(client, "SELECT * FROM high_value_events WHERE user_id = 123")
        results = await reader.query()
        print(results)
        
        # Or use Query builder with the view
        query = Query(high_value_events).filter(
            high_value_events.user_id == 123
        )
        reader = Reader(client, query)
        results = await reader.query()
        
        # Or stream results
        reader = Reader(client, "SELECT * FROM high_value_events")
        results = await reader.stream()
        async for row in results:
            print(row)
```

---

## Materialized Views

Materialized views store computed results in a backing table. They automatically insert rows into the backing table when data is inserted into the source table.

### Creating a Materialized View

Materialized views require:
1. A source table to watch
2. A backing table to store results
3. A query to transform/aggregate the data

```py
from pyclickhouse import View, Table, Query, F, Aggregate
from pydantic import BaseModel
from datetime import datetime
from typing import Annotated
from pyclickhouse import Column

class Hourly(BaseModel):
    domain: str
    timestamp: datetime
    count: int

class Daily(BaseModel):
    domain: Annotated[str, Column(type="String")]
    date: Annotated[str, Column(type="Date")]
    total_count: Annotated[int, Column(type="UInt64")]

hourly_table = Table(model=Hourly, name="hourly_data")
daily_table = Table(model=Daily, name="daily_data")

# Create materialized view that aggregates hourly data to daily
daily_mv = View(
    name="daily_aggregated_mv",
    select=Query(hourly_table).group(
        domain=hourly_table.domain,
        date=F.toDate(hourly_table.timestamp),
        total_count=Aggregate(F.sum(hourly_table.count))
    ),
    table=daily_table  # Backing table for materialized results
)
```

### How Materialized Views Work

1. **Data flows**: When data is inserted into `hourly_table`, it automatically triggers the view's SELECT query
2. **Results stored**: The query result rows are inserted into `daily_table`
3. **Backing table**: The `daily_table` stores the actual materialized data
4. **Query the table**: You query the backing table to access materialized results, not the view

```py
from pyclickhouse import Client, Reader, Query

async def work_with_materialized_view():
    client = Client()
    
    async with client:
        # Query the backing table (where data is actually stored)
        query = Query(daily_table)
        reader = Reader(client, query)
        results = await reader.query()
        
        # You can also aggregate from the backing table
        agg_query = Query(daily_table).group(
            domain=daily_table.domain,
            total=Aggregate(F.sum(daily_table.total_count))
        )
        reader = Reader(client, agg_query)
        results = await reader.query()
```

### Materialized View Example: Counting Events

```py
from pyclickhouse import View, Table, Query, F, Aggregate
from pydantic import BaseModel
from typing import Annotated
from pyclickhouse import Column

class Event(BaseModel):
    timestamp: str
    event_type: str
    user_id: int

class EventStats(BaseModel):
    event_type: Annotated[str, Column(type="String")]
    count: Annotated[int, Column(type="UInt64")]

events = Table(model=Event, name="events")
event_stats = Table(model=EventStats, name="event_stats")

# Materialized view that counts events by type
event_count_mv = View(
    name="event_count_mv",
    select=Query(events).group(
        event_type=events.event_type,
        count=Aggregate(F.count())
    ),
    table=event_stats
)
```

---

## Advanced Aggregations with Materialized Views

Materialized views can use aggregate functions to build complex data warehouses.

### State and Merge Functions

For intermediate aggregations, use `sumState()` and `sumMerge()` pattern:

```py
from pyclickhouse import View, Table, Query, F, Aggregate
from pydantic import BaseModel
from typing import Annotated
from pyclickhouse import Column
from datetime import datetime

class Hourly(BaseModel):
    domain: str
    event_time: datetime
    count_views: int

class Monthly(BaseModel):
    domain: Annotated[str, Column(type="String")]
    month: Annotated[str, Column(type="Date")]
    sum_count_views: Annotated[
        int, 
        Column(type="AggregateFunction(sum, UInt64)")
    ]

hourly = Table(Hourly, name="hourly_data")
monthly = Table(Monthly, name="monthly_data")

# Store intermediate sum state in the backing table
select_query = Query(hourly).group(
    domain=hourly.domain,
    month=F.toDate(F.toStartOfMonth(hourly.event_time)),
    sum_count_views=Aggregate(F.sumState(hourly.count_views))
)

monthly_aggregated_mv = View(
    name="monthly_aggregated_mv",
    select=select_query,
    table=monthly
)

# Later, merge the states for final result
async def get_monthly_summary():
    from pyclickhouse import Client, Reader
    client = Client()
    
    async with client:
        summary_query = Query(monthly).group(
            domain=monthly.domain,
            month=monthly.month,
            sum_count_views=Aggregate(F.sumMerge(monthly.sum_count_views))
        )
        reader = Reader(client, summary_query)
        results = await reader.query()
        return results
```

---

## Creating and Managing Views

### Creating Views with Admin

Use the `Admin` class to create views in ClickHouse. The `create_view()` method automatically handles both simple and materialized views:

```py
from pyclickhouse import Client, Admin, View, Table, Query

async def create_views():
    client = Client()
    admin = Admin(client)
    
    async with client:
        # Create simple view (no backing table)
        simple_view = View(
            name="user_summary",
            select=Query(events).filter(events.value > 100)
        )
        await admin.create_view(simple_view)
        
        # Create materialized view (with backing table)
        mv = View(
            name="daily_stats",
            select=Query(events).group(
                date=F.toDate(events.timestamp),
                total=Aggregate(F.sum(events.value))
            ),
            table=stats_table  # Specifying table makes it materialized
        )
        await admin.create_view(mv)
```

### Creating All Views from Registry

Views are automatically registered with `default_registry`. Create all views at once:

```py
from pyclickhouse import Client, Admin, default_registry

async def setup_all():
    client = Client()
    admin = Admin(client)
    
    async with client:
        # Create all tables and views from registry
        await admin.create_all(default_registry)
```

### Dropping Views

```py
async def drop_views():
    client = Client()
    admin = Admin(client)
    
    async with client:
        # Drop a view
        await admin.drop_view(daily_mv)
        
        # Drop if exists
        await admin.drop_view(daily_mv, if_exists=True)
```

---

## Integration Engines

### Kafka Engine

Use the Kafka engine to consume data from Kafka topics into ClickHouse:

```py
from pyclickhouse import Table, engines
from pydantic import BaseModel

class KafkaEvent(BaseModel):
    timestamp: str
    user_id: int
    event_type: str
    value: float

# Create a Kafka table to consume events from a topic
kafka_events = Table(
    model=KafkaEvent,
    name="kafka_events",
    engine=engines.Kafka(
        broker_list="localhost:9092",
        topic_list="events",
        group_name="clickhouse_consumer",
        format="JSONEachRow"
    )
)

# Create a materialized view to move data from Kafka to a persistent table
events_storage = Table(
    model=KafkaEvent,
    name="events_storage",
    engine=engines.MergeTree(order_by="timestamp")
)

kafka_to_storage = View(
    name="kafka_to_storage_mv",
    select=Query(kafka_events),
    table=events_storage
)
```

### Using Kafka in Practice

```py
from pyclickhouse import Client, Admin, Reader, Query

async def consume_kafka_events():
    client = Client()
    admin = Admin(client)
    
    async with client:
        # Create Kafka table and materialized view
        await admin.create_table(kafka_events)
        await admin.create_table(events_storage)
        await admin.create_view(kafka_to_storage)
        
        # Query the persistent storage table
        # (data flows automatically from Kafka via the materialized view)
        query = Query(events_storage).filter(
            events_storage.event_type == "purchase"
        )
        reader = Reader(client, query)
        results = await reader.query()
        
        for row in results:
            print(f"Purchase event: user {row['user_id']} - value {row['value']}")
        
        # Stream new events as they arrive
        stream_reader = Reader(client, query)
        results = await stream_reader.stream()
        async for row in results:
            print(f"New event: {row}")
```

### Kafka Integration Example: Event Processing

```py
from pyclickhouse import Table, View, Query, F, Aggregate, engines
from pydantic import BaseModel
from typing import Annotated
from pyclickhouse import Column

class RawEvent(BaseModel):
    timestamp: str
    user_id: int
    event_type: str
    duration: int

# Kafka table for raw events
raw_events = Table(
    model=RawEvent,
    name="raw_events",
    engine=engines.Kafka(
        broker_list="kafka:9092",
        topic_list="raw_events",
        group_name="event_processor",
        format="JSONEachRow"
    )
)

# Persistent storage
class EventStorage(BaseModel):
    timestamp: str
    user_id: Annotated[int, Column(type="Int32")]
    event_type: str
    duration: int

events_table = Table(
    model=EventStorage,
    name="events",
    engine=engines.MergeTree(
        order_by="timestamp",
        partition_by="toYYYYMM(timestamp)"
    )
)

# Materialized view: pipe Kafka -> storage
kafka_ingestion = View(
    name="kafka_ingestion_mv",
    select=Query(raw_events),
    table=events_table
)

# Another materialized view: aggregate statistics
class EventStats(BaseModel):
    event_type: Annotated[str, Column(type="String")]
    count: Annotated[int, Column(type="UInt64")]
    avg_duration: Annotated[int, Column(type="AggregateFunction(avg, Int32)")]

stats_table = Table(
    model=EventStats,
    name="event_stats",
    engine=engines.ReplacingMergeTree(order_by="event_type")
)

event_stats_mv = View(
    name="event_stats_mv",
    select=Query(events_table).group(
        event_type=events_table.event_type,
        count=Aggregate(F.count()),
        avg_duration=Aggregate(F.avgState(events_table.duration))
    ),
    table=stats_table
)
```

---

### PostgreSQL Engine

Use the PostgreSQL engine to read or write data from PostgreSQL tables:

```py
from pyclickhouse import Table, engines
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

# Create a PostgreSQL table that reads from a remote PostgreSQL database
pg_users = Table(
    model=User,
    name="pg_users",
    engine=engines.PostgreSQL(
        host_port="postgres-host:5432",
        database="production",
        table="users",
        user="clickhouse_user",
        password="secure_password"
    )
)
```

### Reading from PostgreSQL

```py
from pyclickhouse import Client, Reader, Query, F, Aggregate

async def read_postgres_data():
    client = Client()
    
    async with client:
        # Query PostgreSQL table directly
        query = Query(pg_users).filter(pg_users.id > 100)
        reader = Reader(client, query)
        results = await reader.query()
        
        for row in results:
            print(f"User {row['id']}: {row['name']} ({row['email']})")
        
        # Aggregate PostgreSQL data in ClickHouse
        agg_query = Query(pg_users).aggregate(
            total_users=Aggregate(F.count()),
            user_count=Aggregate(F.uniq(pg_users.id))
        )
        reader = Reader(client, agg_query)
        results = await reader.query()
        print(f"Total users: {results[0]['total_users']}")
```

### PostgreSQL Integration Example: Syncing Data

```py
from pyclickhouse import Table, View, Query, engines
from pydantic import BaseModel
from typing import Annotated
from pyclickhouse import Column

class PostgreSQLUser(BaseModel):
    id: int
    name: str
    email: str
    created_at: str

# PostgreSQL source table
pg_source = Table(
    model=PostgreSQLUser,
    name="pg_users_source",
    engine=engines.PostgreSQL(
        host_port="postgres:5432",
        database="app_db",
        table="users",
        user="reader",
        password="password"
    )
)

# ClickHouse local cache/denormalization
class UserCache(BaseModel):
    id: Annotated[int, Column(type="Int32")]
    name: str
    email: str
    created_at: str

users_cache = Table(
    model=UserCache,
    name="users_cache",
    engine=engines.MergeTree(order_by="id")
)

# Materialized view to sync PostgreSQL -> ClickHouse
postgres_sync_mv = View(
    name="postgres_sync_mv",
    select=Query(pg_source),
    table=users_cache
)
```

### Querying Synced PostgreSQL Data

```py
from pyclickhouse import Client, Admin, Reader

async def query_synced_data():
    client = Client()
    admin = Admin(client)
    
    async with client:
        # Create materialized view to sync data
        await admin.create_view(postgres_sync_mv)
        
        # Query the synced data (very fast - stored in ClickHouse)
        reader = Reader(client, "SELECT * FROM users_cache WHERE id > 50")
        results = await reader.query()
        
        for row in results:
            print(f"User: {row['name']} ({row['email']})")
        
        # Perform analytics on synced data
        stats_query = """
            SELECT 
                COUNT(*) as total_users,
                COUNT(DISTINCT email) as unique_emails
            FROM users_cache
        """
        reader = Reader(client, stats_query)
        results = await reader.query()
        print(f"Stats: {results[0]}")
```

---

## View Lifecycle

Views support lifecycle management like tables:

```py
from pyclickhouse import View, Lifecycle

# Managed view (default) - ORM can create, alter, drop
managed_view = View(
    name="my_view",
    select="SELECT * FROM events WHERE value > 100"
)

# Protected view - ORM won't drop or modify
protected_view = View(
    name="prod_view",
    select="SELECT * FROM events WHERE value > 100",
    lifecycle=Lifecycle.protected
)

# External view - ORM treats as read-only
external_view = View(
    name="legacy_view",
    select="SELECT * FROM events WHERE value > 100",
    lifecycle=Lifecycle.external
)
```

---

## Auto-Registration

Views are automatically registered with `default_registry` when created:

```py
from pyclickhouse import View, default_registry

# Auto-registered
my_view = View(
    name="stats",
    select="SELECT COUNT(*) as total FROM events"
)

# Access from registry
view = default_registry.get_view("stats")
all_views = default_registry.list_views()
```

### Disable Auto-Registration

To prevent auto-registration, pass `registry=None`:

```py
# Not registered with default_registry
temp_view = View(
    name="temp_stats",
    select="SELECT * FROM events LIMIT 100",
    registry=None
)
```

---

## Complete Example with Kafka and PostgreSQL

```py
from pyclickhouse import (
    Client, Admin, Table, View, Query, Reader, Writer, F, Aggregate,
    Column, engines, default_registry
)
from pydantic import BaseModel
from typing import Annotated
from datetime import datetime

# PostgreSQL source: user information
class PostgreSQLUser(BaseModel):
    id: int
    name: str
    email: str

pg_users = Table(
    model=PostgreSQLUser,
    name="pg_users",
    engine=engines.PostgreSQL(
        host_port="postgres:5432",
        database="app_db",
        table="users",
        user="reader",
        password="password"
    )
)

# Kafka source: user events
class KafkaEvent(BaseModel):
    timestamp: datetime
    user_id: int
    event_type: str
    value: float

kafka_events = Table(
    model=KafkaEvent,
    name="kafka_events",
    engine=engines.Kafka(
        broker_list="kafka:9092",
        topic_list="user_events",
        group_name="analytics",
        format="JSONEachRow"
    )
)

# Local storage for events
class EventStorage(BaseModel):
    timestamp: datetime
    user_id: Annotated[int, Column(type="Int32")]
    event_type: str
    value: float

events_storage = Table(
    model=EventStorage,
    name="events",
    engine=engines.MergeTree(order_by="timestamp")
)

# Local cache for user data
class UserCache(BaseModel):
    id: int
    name: str
    email: str

user_cache = Table(
    model=UserCache,
    name="users",
    engine=engines.MergeTree(order_by="id")
)

# Materialized views to sync data
kafka_sync = View(
    name="kafka_sync_mv",
    select=Query(kafka_events),
    table=events_storage
)

postgres_sync = View(
    name="postgres_sync_mv",
    select=Query(pg_users),
    table=user_cache
)

# Analytics view: events with user information
enriched_events = View(
    name="enriched_events",
    select="""
        SELECT 
            e.timestamp,
            u.name as user_name,
            e.event_type,
            e.value
        FROM events e
        LEFT JOIN users u ON e.user_id = u.id
    """
)

async def main():
    client = Client()
    admin = Admin(client)
    
    async with client:
        # Create all tables and views
        await admin.create_all(default_registry)
        
        # Query synced PostgreSQL data
        print("Users from PostgreSQL:")
        reader = Reader(client, "SELECT * FROM users LIMIT 5")
        results = await reader.query()
        for row in results:
            print(f"  {row['name']} ({row['email']})")
        
        # Query Kafka events
        print("\nRecent events:")
        query = Query(events_storage).sort(-events_storage.timestamp).take(10)
        reader = Reader(client, query)
        results = await reader.query()
        for row in results:
            print(f"  {row['event_type']} - value: {row['value']}")
        
        # Query enriched data
        print("\nEnriched events:")
        reader = Reader(client, "SELECT * FROM enriched_events LIMIT 5")
        results = await reader.query()
        for row in results:
            print(f"  {row['user_name']}: {row['event_type']} ({row['value']})")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

---

## Simple Views vs Materialized Views

### When to Use Simple Views

- **Low-volume queries**: Queries that don't need to be cached
- **Always-current data**: When you need real-time results
- **Complex one-off queries**: Named queries that are rarely executed
- **Low storage constraints**: When you can't afford backing table storage

### When to Use Materialized Views

- **High-volume access**: Frequently queried aggregations
- **Real-time dashboards**: Need fast aggregation results
- **Data pipeline stages**: Multi-step data transformations
- **Pre-aggregated analytics**: Store pre-computed results
- **Complex aggregations**: Heavy GROUP BY with multiple aggregate functions

---

## Learn More

- [Table Concepts](/concepts/table) — Understanding table definitions
- [Query Builder](/concepts/query) — Building complex queries
- [Admin API](/concepts/admin) — Managing databases and schemas
- [Reader](/concepts/reader) — Querying and streaming data
- [Writer](/concepts/writer) — Inserting data into tables
