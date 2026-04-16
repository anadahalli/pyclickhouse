---
title: Admin
---

The `Admin` class provides administrative operations for managing ClickHouse databases, tables, views, and columns. It handles schema creation, modification, deletion, and migrations.

---

## Creating an Admin Instance

Initialize an Admin instance with a connected client:

```py
from pyclickhouse import Admin, Client

client = Client()

async with client:
    admin = Admin(client)
    # perform admin operations
```

### Specifying a Database

By default, Admin operates on the client's database. You can specify a different database:

```py
async with client:
    admin = Admin(client, database="analytics")
    # operations are now on the "analytics" database
```

### Cluster Operations

For cluster environments, specify the cluster name:

```py
async with client:
    admin = Admin(client, cluster="my_cluster")
    # operations are distributed across the cluster
```

---

## Database Operations

### Show Databases

List all available databases:

```py
async with client:
    admin = Admin(client)
    databases = await admin.show_databases()
    print(databases)
    # ["default", "analytics", "system", ...]
```

### Create Database

Create a new database:

```py
async with client:
    admin = Admin(client)
    await admin.create_datbase("analytics")
```

### Drop Database

Drop a database:

```py
async with client:
    admin = Admin(client)
    await admin.drop_datbase("analytics")
```

---

## Table Operations

### Create Table

Create a table from a Pydantic model:

```py
from pydantic import BaseModel
from pyclickhouse import Table

class Event(BaseModel):
    id: int
    name: str
    timestamp: str

events = Table(model=Event, name="events")

async with client:
    admin = Admin(client)
    await admin.create_table(events)
```

### Show Tables

List all tables in the database:

```py
async with client:
    admin = Admin(client)
    tables = await admin.show_tables()
    for table in tables:
        print(table)
```

### Get Table

Retrieve a table definition:

```py
async with client:
    admin = Admin(client)
    table = await admin.get_table("events")
```

### Show Create Table

Display the SQL statement for creating a table:

```py
async with client:
    admin = Admin(client)
    sql = await admin.show_create_table("events")
    print(sql)
```

### Drop Table

Drop a table from the database:

```py
async with client:
    admin = Admin(client)
    await admin.drop_table("events")
```

### Truncate Table

Remove all data from a table (keeps structure):

```py
async with client:
    admin = Admin(client)
    await admin.truncate_table("events")
```

### Copy Table

Create a copy of an existing table:

```py
async with client:
    admin = Admin(client)
    await admin.copy_table("events", "events_backup")
```

### Diff Table

Compare a table definition with a model:

```py
async with client:
    admin = Admin(client)
    differences = await admin.diff_table("events", events)
    print(differences)
```

### Alter Table

Modify table properties:

```py
async with client:
    admin = Admin(client)
    await admin.alter_table("events", "ORDER BY timestamp")
```

---

## Column Operations

### Add Column

Add a new column to a table:

```py
from pyclickhouse import Column

async with client:
    admin = Admin(client)
    await admin.add_column("events", Column(name="user_id", type="Int32"))
```

### Drop Column

Remove a column from a table:

```py
async with client:
    admin = Admin(client)
    await admin.drop_column("events", "user_id")
```

### Modify Column

Change a column's properties:

```py
async with client:
    admin = Admin(client)
    await admin.modify_column("events", Column(name="user_id", type="String"))
```

---

## View Operations

### Show Views

List all views in the database:

```py
async with client:
    admin = Admin(client)
    views = await admin.show_views()
```

### Create Simple View

Create a standard view:

```py
from pyclickhouse import View

async with client:
    admin = Admin(client)
    view = View(
        name="events_daily",
        query="SELECT toDate(timestamp) as date, count() as count FROM events GROUP BY date"
    )
    await admin.create_simple_view(view)
```

### Create Materialized View

Create a materialized view with a target table:

```py
async with client:
    admin = Admin(client)
    view = View(
        name="events_daily_mv",
        query="SELECT toDate(timestamp) as date, count() as count FROM events GROUP BY date",
        target_table="events_daily_data"
    )
    await admin.create_materialized_view(view)
```

### Drop View

Remove a view:

```py
async with client:
    admin = Admin(client)
    await admin.drop_view("events_daily")
```

### Get View

Retrieve a view definition:

```py
async with client:
    admin = Admin(client)
    view = await admin.get_view("events_daily")
```

---

## Batch Operations

### Create All

Create all tables and views registered in the default registry:

```py
async with client:
    admin = Admin(client)
    await admin.create_all()
```

### Drop All

Drop all tables and views:

```py
async with client:
    admin = Admin(client)
    await admin.drop_all()
```

---

## Migrations

### Migrate Table

Migrate a table schema to match a model:

```py
async with client:
    admin = Admin(client)
    await admin.migrate_table("events", events)
```

### Migrate View

Migrate a view definition:

```py
async with client:
    admin = Admin(client)
    await admin.migrate_view("events_daily", view)
```

### Migrate All

Migrate all registered tables and views:

```py
async with client:
    admin = Admin(client)
    await admin.migrate_all()
```

---

## Create Model from SQL

Generate a Pydantic model from an existing table:

```py
async with client:
    admin = Admin(client)
    model = await admin.create_model("events")
    print(model)
    # <class 'Event'>
```

---

## Error Handling

The Admin class raises `AdminError` for operational failures:

```py
from pyclickhouse import AdminError

async with client:
    admin = Admin(client)
    try:
        await admin.create_table(existing_table)
    except AdminError as e:
        print(f"Admin error: {e}")
```

---

## Complete Example

Here's a complete example combining multiple admin operations:

```py
from pydantic import BaseModel
from pyclickhouse import Admin, Client, Table

class Event(BaseModel):
    id: int
    name: str
    timestamp: str
    value: float

async def setup_database():
    client = Client()
    
    events = Table(model=Event, name="events")
    
    async with client:
        admin = Admin(client, database="analytics")
        
        # Create the table
        await admin.create_table(events)
        
        # Show table info
        sql = await admin.show_create_table("events")
        print(sql)
        
        # Add a new column
        from pyclickhouse import Column
        await admin.add_column("events", Column(name="user_id", type="Int32"))
        
        # Create an aggregation view
        from pyclickhouse import View
        view = View(
            name="events_summary",
            query="SELECT name, sum(value) as total FROM events GROUP BY name"
        )
        await admin.create_simple_view(view)
        
        # List all tables and views
        tables = await admin.show_tables()
        views = await admin.show_views()
        print(f"Tables: {tables}, Views: {views}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(setup_database())
```

---

Learn more about the [Admin API](/references/admin), [Table definitions](/concepts/table), and [Views](/concepts/view).