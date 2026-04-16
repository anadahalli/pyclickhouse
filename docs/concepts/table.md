---
title: Table
---

The `Table` class represents a ClickHouse table definition backed by a Pydantic model. It automatically maps Python types to ClickHouse column types and provides a type-safe way to define table schemas.

---

## Creating a Table

### From a Pydantic Model

Create a table from a Pydantic model:

```py
from pydantic import BaseModel
from pyclickhouse import Table

class User(BaseModel):
    id: int
    name: str
    email: str

users = Table(model=User)
```

By default, the table name is the snake_case version of the model name (`user`). Column names and types are automatically derived from the model fields.

### Customizing the Table Name

```py
users = Table(model=User, name="users_table")
```

### With a Custom Engine

Specify the table engine using the engines module:

```py
from pyclickhouse import Table, engines

users = Table(
    model=User,
    name="users",
    engine=engines.MergeTree(
        order_by="id",
        partition_by="toYYYYMM(updated_at)"
    )
)
```

Or use a string:

```py
users = Table(
    model=User,
    engine="ReplacingMergeTree() ORDER BY id"
)
```

### Available Engines

Common engines include:

```py
from pyclickhouse import engines

# MergeTree family
engines.MergeTree(order_by="id")
engines.ReplacingMergeTree(order_by="id", ver="version")
engines.AggregatingMergeTree(order_by="id")
engines.CollapsingMergeTree(order_by="id", sign="sign")
engines.VersionedCollapsingMergeTree(order_by="id", sign="sign", version="version")

# Other engines
engines.Memory()
engines.Kafka(...)
engines.PostgreSQL(...)
```

### With Comments

Add a comment to the table:

```py
users = Table(
    model=User,
    comment="User profile information"
)
```

---

## Columns

### Automatic Column Detection

Columns are automatically created from Pydantic model fields:

```py
class Event(BaseModel):
    id: int  # Maps to Int64
    name: str  # Maps to String
    value: float  # Maps to Float64
    timestamp: str  # Maps to String

events = Table(model=Event)

# Access columns via the table
columns = events.get_columns()
for col_name, col in columns.items():
    print(f"{col_name}: {col.type}")
```

### Customizing Columns with Annotated

Use `typing.Annotated` to customize column properties:

```py
from typing import Annotated
from pydantic import BaseModel
from pyclickhouse import Table, Column

class Event(BaseModel):
    id: int
    event_name: Annotated[str, Column(comment="Name of the event")]
    value: Annotated[float, Column(comment="Event value")]

events = Table(model=Event)
```

### Customizing Columns with Annotated and Field

Combine `Annotated` with `pydantic.Field` for full control:

```py
from typing import Annotated
from pydantic import BaseModel, Field
from pyclickhouse import Table, Column

class Event(BaseModel):
    id: int = Field(description="Event ID")
    timestamp: Annotated[str, Column(
        comment="Event timestamp",
        codec_expression="ZSTD(1)",
        ttl_expression="timestamp + INTERVAL 30 DAY"
    )] = Field(description="When the event occurred")
    event_name: Annotated[str, Column(comment="Event name")]
    value: Annotated[float, Column(comment="Event value")]

events = Table(model=Event)
```

### Column with All Properties

Add comments, codecs, and TTL to columns:

```py
from typing import Annotated
from pydantic import BaseModel, Field
from pyclickhouse import Column, Table

class Event(BaseModel):
    timestamp: Annotated[str, Column(
        comment="Event timestamp",
        codec_expression="ZSTD(1)",
        ttl_expression="timestamp + INTERVAL 30 DAY",
        default_type="DEFAULT",
        default_expression="now()"
    )] = Field(description="When the event occurred")
    event_name: str
    value: float

events = Table(model=Event)
```

### Column Properties Reference

The `Column` class accepts the following properties:

- **`name`**: Column name (auto-detected from field name)
- **`type`**: ClickHouse type (auto-detected from Python type)
- **`comment`**: Description of the column
- **`codec_expression`**: Compression codec (e.g., "ZSTD(1)")
- **`ttl_expression`**: TTL (Time To Live) expression
- **`default_type`**: DEFAULT or MATERIALIZED
- **`default_expression`**: Default value expression

### Custom Column Names and Types

Use the `name` parameter to use a different column name in the database than in your Python model:

```py
from typing import Annotated
from pydantic import BaseModel
from pyclickhouse import Table, Column

class User(BaseModel):
    user_id: Annotated[int, Column(name="id")]  # Python field "user_id" -> DB column "id"
    full_name: Annotated[str, Column(name="name")]  # Python field "full_name" -> DB column "name"
    email_address: Annotated[str, Column(name="email")]

users = Table(model=User)

# The table will have columns: id, name, email (not user_id, full_name, email_address)
```

Use the `type` parameter to specify a custom ClickHouse type:

```py
from typing import Annotated
from pydantic import BaseModel
from pyclickhouse import Table, Column

class Product(BaseModel):
    id: int
    price: Annotated[float, Column(type="Decimal(10, 2)")]  # Custom Decimal with precision
    description: Annotated[str, Column(type="String")]  # Explicit String type
    tags: Annotated[list[str], Column(type="Array(String)")]  # Explicit Array type

products = Table(model=Product)
```

Combine custom `name` and `type`:

```py
from typing import Annotated
from pydantic import BaseModel
from pyclickhouse import Table, Column

class Order(BaseModel):
    order_id: Annotated[int, Column(
        name="id",
        type="UInt32"  # Use UInt32 instead of Int64
    )]
    order_amount: Annotated[float, Column(
        name="amount",
        type="Decimal(18, 4)",
        comment="Order total in currency"
    )]
    order_date: Annotated[str, Column(
        name="created_date",
        type="Date",
        comment="Date order was placed"
    )]

orders = Table(model=Order)

# The table will have columns: id (UInt32), amount (Decimal(18, 4)), created_date (Date)
```

### Advanced Column Configuration

Combine all Column parameters for full control:

```py
from typing import Annotated
from pydantic import BaseModel, Field
from pyclickhouse import Table, Column

class Analytics(BaseModel):
    metric_id: Annotated[int, Column(
        name="id",
        type="UInt64",
        comment="Unique metric identifier"
    )]
    metric_value: Annotated[float, Column(
        name="value",
        type="Float32",  # Use Float32 instead of Float64 to save space
        comment="Metric measurement value",
        codec_expression="ZSTD(3)",  # Compression codec
        default_type="DEFAULT",
        default_expression="0.0"
    )]
    timestamp: Annotated[str, Column(
        name="recorded_at",
        type="DateTime",
        comment="When metric was recorded",
        ttl_expression="recorded_at + INTERVAL 1 YEAR"  # Auto-delete after 1 year
    )]
    dimensions: Annotated[dict, Column(
        name="tags",
        type="Map(String, String)",
        comment="Dimension tags"
    )]

analytics = Table(model=Analytics)
```

### Getting Column Information

```py
events = Table(model=Event)

# Get all columns
columns = events.get_columns()

# Iterate over columns
for col_name, col in columns.items():
    print(f"Column: {col_name}")
    print(f"  Type: {col.type}")
    print(f"  Comment: {col.comment}")
    print(f"  DB Name: {col.name}")  # Shows the actual database column name
```

### Custom Data Types for Columns

#### Using Optional Types

Create nullable columns using `Optional` or `Union[Type, None]`:

```py
from typing import Optional, Annotated
from pydantic import BaseModel
from pyclickhouse import Table, Column

class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    tags: Optional[list[str]] = None
    price: float
    discount: Optional[float] = None

products = Table(model=Product)

# Columns will be:
# - id: Int64
# - name: String
# - description: Nullable(String)
# - tags: Nullable(Array(String))
# - price: Float64
# - discount: Nullable(Float64)
```

#### Using Array Types

Store collections of data:

```py
from typing import List, Annotated
from pydantic import BaseModel
from pyclickhouse import Table, Column

class BlogPost(BaseModel):
    id: int
    title: str
    tags: List[str]
    categories: Annotated[List[str], Column(comment="Content categories")]
    ratings: List[float]
    comments_count: int

posts = Table(model=BlogPost)

# Columns will be:
# - tags: Array(String)
# - categories: Array(String)
# - ratings: Array(Float64)
```

#### Using Tuple Types

Store fixed-size structured data:

```py
from typing import Tuple, Annotated
from pydantic import BaseModel
from pyclickhouse import Table, Column

class LocationEvent(BaseModel):
    event_id: int
    coordinates: Tuple[float, float]
    location_info: Annotated[Tuple[str, str, int], Column(comment="City, Country, Zip")]
    timestamp: str

events = Table(model=LocationEvent)

# Columns will be:
# - coordinates: Tuple(Float64, Float64)
# - location_info: Tuple(String, String, Int64)
```

#### Using Map/Dict Types

Store key-value data:

```py
from typing import Dict
from pydantic import BaseModel
from pyclickhouse import Table, Column

class MetricsData(BaseModel):
    event_id: int
    properties: Dict[str, str]
    numeric_metrics: Dict[str, float]
    tags: Dict[str, int]

metrics = Table(model=MetricsData)

# Columns will be:
# - properties: Map(String, String)
# - numeric_metrics: Map(String, Float64)
# - tags: Map(String, Int64)
```

#### Using Date and DateTime Types

Store temporal data:

```py
from datetime import date, datetime
from typing import Annotated
from pydantic import BaseModel
from pyclickhouse import Table, Column

class TimeSeriesEvent(BaseModel):
    event_date: date
    created_at: datetime
    updated_at: Annotated[datetime, Column(comment="Last update timestamp")]

events = Table(model=TimeSeriesEvent)

# Columns will be:
# - event_date: Date
# - created_at: DateTime
# - updated_at: DateTime
```

#### Using Enum Types

Store enumerated values:

```py
from enum import StrEnum, auto
from typing import Annotated
from pydantic import BaseModel
from pyclickhouse import Table, Column

class Status(StrEnum):
    PENDING = auto()
    ACTIVE = auto()
    INACTIVE = auto()
    ARCHIVED = auto()

class Task(BaseModel):
    id: int
    title: str
    status: Annotated[Status, Column(comment="Task status")]

tasks = Table(model=Task)

# Columns will be:
# - status: Enum('PENDING', 'ACTIVE', 'INACTIVE', 'ARCHIVED')
```

#### Using UUID Type

Store universally unique identifiers:

```py
from uuid import UUID
from typing import Annotated
from pydantic import BaseModel
from pyclickhouse import Table, Column

class Account(BaseModel):
    account_id: Annotated[UUID, Column(comment="Unique account identifier")]
    user_id: UUID
    created_at: str

accounts = Table(model=Account)

# Columns will be:
# - account_id: UUID
# - user_id: UUID
```

#### Using Decimal Type

Store precise decimal numbers:

```py
from decimal import Decimal
from typing import Annotated
from pydantic import BaseModel
from pyclickhouse import Table, Column

class Transaction(BaseModel):
    transaction_id: int
    amount: Decimal
    tax: Annotated[Decimal, Column(comment="Tax amount")]
    total: Decimal

transactions = Table(model=Transaction)

# Columns will be:
# - amount: Decimal
# - tax: Decimal
# - total: Decimal
```

#### Using IP Address Types

Store IP addresses:

```py
from ipaddress import IPv4Address, IPv6Address
from typing import Optional, Annotated
from pydantic import BaseModel
from pyclickhouse import Table, Column

class ConnectionLog(BaseModel):
    connection_id: int
    client_ipv4: Optional[IPv4Address] = None
    client_ipv6: Optional[IPv6Address] = None
    server_ip: Annotated[IPv4Address, Column(comment="Server IP address")]

logs = Table(model=ConnectionLog)

# Columns will be:
# - client_ipv4: Nullable(IPv4)
# - client_ipv6: Nullable(IPv6)
# - server_ip: IPv4
```

---

## Expressions and Column References

### Accessing Columns as Expressions

Access table columns using attribute notation. This returns an `Expression` that can be used in queries:

```py
users = Table(model=User)

# Access column as expression
user_id_expr = users.id
user_name_expr = users.name

# Use in filters
print(str(users.id))  # "users.id"
print(str(users.name == "Alice"))  # "users.name == 'Alice'"
```

The `Expression` class represents a query expression that can be combined with operators to build complex filter conditions.

### Comparison Operators

Expressions support all comparison operators for creating filter conditions:

```py
users = Table(model=User)

# Greater than
users.id > 10

# Greater than or equal
users.id >= 10

# Less than
users.id < 100

# Less than or equal
users.id <= 100

# Equals
users.name == "Alice"

# Not equals
users.name != "Bob"
```

### Arithmetic Operations

```py
events = Table(model=Event)

# Addition
events.value + 10

# Subtraction
events.value - 5

# Multiplication
events.value * 2

# Division
events.value / 2
```

### Logical Operations

Combine multiple conditions using logical operators:

```py
# AND - both conditions must be true
query = Query(users).filter(
    (users.id > 10) & (users.name == "Alice")
)

# OR - either condition can be true
query = Query(users).filter(
    (users.name == "Alice") | (users.name == "Bob")
)

# NOT - negate a condition
query = Query(users).filter(~(users.id == 0))
```

### IN and NOT IN

Check if a column value is in or not in a list:

```py
# Check if column is in list
query = Query(users).filter(users.id.is_in([1, 2, 3, 4, 5]))

# Check if column is NOT in list
query = Query(users).filter(users.name.is_not_in(["spam", "bot"]))
```

### Using Expressions in Filters

```py
from pyclickhouse import Query

users = Table(model=User)

# Simple filter
query = Query(users).filter(users.id > 10)

# Complex filter with multiple conditions
query = Query(users).filter(
    (users.id > 10) & 
    (users.name != "admin") &
    (users.email.is_in(["alice@example.com", "bob@example.com"]))
)
```

### Using Expressions in SELECT

Pass column expressions to select specific columns:

```py
# Select specific columns
query = Query(users).select(users.id, users.name)

# With custom column names
query = Query(users).select(
    user_id=users.id,
    full_name=users.name
)
```

### Using Expressions in DERIVE (Computed Columns)

Create computed columns based on existing columns:

```py
from pyclickhouse import F

# Add computed columns
query = Query(users).derive(
    name_lower=F.lower(users.name),
    name_length=F.length(users.name)
)
```

### Using Expressions in GROUP BY

```py
# Group by a column
query = Query(events).group(events.event_name)

# Group by multiple columns
query = Query(events).group(events.event_name, events.user_id)
```

### Using Expressions in Aggregations

```py
from pyclickhouse import F

events = Table(model=Event)

# Group and aggregate
query = Query(events).group(events.event_name).aggregate(
    total=F.sum(events.value),
    count=F.count(),
    avg_value=F.avg(events.value),
    max_value=F.max(events.value)
)
```

### Using Expressions in SORT

```py
# Ascending order (default)
query = Query(users).sort(users.id)

# Descending order
query = Query(users).sort(-users.id)

# Sort by multiple columns
query = Query(events).sort(events.event_name, -events.value)
```

### Expression String Representation

Get the SQL representation of an expression:

```py
users = Table(model=User)

expr = users.id > 10
print(str(expr))  # "users.id > 10"

expr = users.name == "Alice"
print(str(expr))  # "users.name == 'Alice'"

expr = (users.id > 10) & (users.name != "Bob")
print(str(expr))  # "users.id > 10 && users.name != 'Bob'"
```

---

## Table Information

### Get Table Metadata

```py
users = Table(model=User, name="users")

# Get the table name
name = users.get_name()  # "users"

# Get the model class
model = users.get_model()  # <class 'User'>

# Get the engine
engine = users.get_engine()  # "MergeTree() ORDER BY ()"

# Get all columns
columns = users.get_columns()  # dict of columns

# Get lifecycle
lifecycle = users.get_lifecycle()  # Lifecycle.managed
```

### String Representation

```py
users = Table(model=User)

print(str(users))  # "users"
print(repr(users))  # "Table(users)"
```

---

## Table Lifecycle

Tables can have different lifecycle states that control how the ORM manages them. The lifecycle determines whether the ORM can create, alter, drop, or migrate the table.

### Lifecycle States

PyClickHouse supports three lifecycle states:

- **`managed`** (default): The ORM has full control. Tables can be created, altered, dropped, and migrated.
- **`protected`**: The ORM can create and read tables, but cannot drop or modify columns. Use for shared/production tables.
- **`external`**: The ORM treats the table as read-only and external. No creation, modification, or deletion allowed.

### Creating Tables with Lifecycle

```py
from pyclickhouse import Table, Lifecycle
from pydantic import BaseModel

class Event(BaseModel):
    id: int
    name: str

# Managed table (default) - full ORM control
managed_table = Table(model=Event, lifecycle=Lifecycle.managed)

# Protected table - ORM can create/read but not drop/modify
protected_table = Table(
    model=Event,
    lifecycle=Lifecycle.protected,
    name="shared_events"
)

# External/unmanaged table - read-only from ORM perspective
external_table = Table(
    model=Event,
    lifecycle=Lifecycle.external,
    name="legacy_events"
)
```

### Checking Lifecycle

```py
table = Table(model=Event)

lifecycle = table.get_lifecycle()
print(lifecycle)  # Lifecycle.managed

if table.get_lifecycle() == Lifecycle.managed:
    print("ORM has full control over this table")
elif table.get_lifecycle() == Lifecycle.protected:
    print("ORM can create/read but not modify")
elif table.get_lifecycle() == Lifecycle.external:
    print("Table is external/read-only")
```

---

## Table Registry

Tables are automatically registered with the default global registry when created. This enables batch operations like creating, migrating, or dropping multiple tables together.

### Auto-Registration

When you create a table, it's automatically registered:

```py
from pyclickhouse import Table
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

# Automatically registered with default_registry
users = Table(model=User)

# Access from default registry
from pyclickhouse.registry import default_registry
same_table = default_registry.get_table("user")
```

### Custom Registry

Create a custom registry if you want to manage tables separately:

```py
from pyclickhouse import Table, Registry
from pydantic import BaseModel

class Event(BaseModel):
    id: int
    user_id: int

# Create custom registry (tables won't auto-register to default)
custom_registry = Registry()

# Manually register with custom registry
events = Table(model=Event, registry=custom_registry)

# List tables in custom registry
for table in custom_registry.list_tables():
    print(f"Table: {table.get_name()}")
```

### Bulk Operations with Registry

Since tables are automatically registered, you can perform bulk operations on all registered tables:

```py
from pyclickhouse import Client, Admin, default_registry
from pydantic import BaseModel
from pyclickhouse import Table

class User(BaseModel):
    id: int
    name: str

class Event(BaseModel):
    event_id: int
    user_id: int
    event_name: str

# Both tables are automatically registered with default_registry
users = Table(model=User)
events = Table(model=Event)

async def setup_database():
    client = Client()
    admin = Admin(client)
    
    async with client:
        # Create all registered tables at once
        await admin.create_all(default_registry)
        
        # Migrate all registered tables
        await admin.migrate_all(default_registry)
        
        # Drop all registered tables
        await admin.drop_all(default_registry)
```

### Disable Auto-Registration

To prevent a table from being automatically registered, use `registry=None`:

```py
from pyclickhouse import Table
from pydantic import BaseModel

class TempTable(BaseModel):
    id: int
    data: str

# This table won't be registered with default_registry
temp = Table(model=TempTable, registry=None)

# Still usable locally, just not included in bulk operations
```

---

## Creating and Managing Tables

### Creating Tables

Use the `Admin` class to create tables in ClickHouse:

```py
from pyclickhouse import Client, Admin, Table, engines
from pydantic import BaseModel

class Event(BaseModel):
    timestamp: str
    event_id: int
    event_name: str
    user_id: int
    value: float

async def create_tables():
    client = Client()
    admin = Admin(client)
    
    async with client:
        # Create a simple table
        events = Table(
            model=Event,
            name="events",
            engine=engines.MergeTree(
                order_by="timestamp",
                partition_by="toYYYYMM(timestamp)"
            ),
            comment="Application events"
        )
        
        await admin.create_table(events)
        print(f"Created table: {events.get_name()}")
```

### Creating Tables with Conditional Logic

```py
async def setup_tables():
    client = Client()
    admin = Admin(client)
    
    async with client:
        events = Table(model=Event, name="events")
        
        # Create only if table doesn't exist (default)
        await admin.create_table(events, if_not_exists=True)
        
        # Create in a specific database
        await admin.create_table(
            events,
            if_not_exists=True,
            database="analytics"
        )
        
        # Create on a cluster
        await admin.create_table(
            events,
            database="analytics",
            cluster="cluster_name"
        )
```

### Dropping Tables

```py
async def drop_tables():
    client = Client()
    admin = Admin(client)
    
    async with client:
        events = Table(model=Event, name="events")
        
        # Drop table (safe - won't error if it doesn't exist)
        await admin.drop_table(events, if_exists=True)
        
        # Drop only if empty
        await admin.drop_table(events, if_empty=True)
        
        # Force drop protected/external tables
        await admin.drop_table(
            events,
            if_exists=True,
            force=True
        )
```

### Truncating Tables

```py
async def truncate_table():
    client = Client()
    admin = Admin(client)
    
    async with client:
        events = Table(model=Event, name="events")
        
        # Clear all data from the table
        await admin.truncate_table(events)
```

---

## Table Reflection and Migration

### Reflecting Existing Tables

Inspect an existing ClickHouse table and create a Pydantic model from its definition:

```py
from pyclickhouse import Client, Admin

async def reflect_table():
    client = Client()
    admin = Admin(client)
    
    async with client:
        # Get table definition from ClickHouse
        table = await admin.get_table("events", database="default")
        
        # Now you have a Table object with columns
        print(f"Table name: {table.get_name()}")
        print(f"Engine: {table.get_engine()}")
        
        # Get the generated Pydantic model
        model = table.get_model()
        
        # Use the model to work with the data
        for col_name, col in table.get_columns().items():
            print(f"  {col_name}: {col.type}")
```

### Creating Models from Query Results

Generate a Pydantic model from query results:

```py
from pyclickhouse import Client, Admin, Query

async def create_model_from_query():
    client = Client()
    admin = Admin(client)
    
    async with client:
        # Create a model from a query result shape
        query = "SELECT user_id, COUNT(*) as count FROM events GROUP BY user_id"
        model = await admin.create_model(query, name="EventStats")
        
        # Use the model
        print(f"Model fields: {model.model_fields.keys()}")
```

### Migrating Tables

Automatically update table schemas to match their Pydantic model definitions:

```py
from pyclickhouse import Client, Admin, Table, Lifecycle
from pydantic import BaseModel

class Event(BaseModel):
    id: int
    name: str
    description: str  # New field
    created_at: str

async def migrate_table():
    client = Client()
    admin = Admin(client)
    
    async with client:
        # Define the table with updated schema
        events = Table(
            model=Event,
            name="events",
            lifecycle=Lifecycle.managed
        )
        
        # Migrate table to match new schema
        # - Adds new columns (description, created_at)
        # - Keeps existing columns
        migrated = await admin.migrate_table(events)
        
        if migrated:
            print("Table migrated successfully")
        else:
            print("Table migration skipped")
```

### Migration Behavior by Lifecycle

Migration behavior depends on the table's lifecycle:

```py
from pyclickhouse import Admin, Table, Lifecycle

admin = Admin(client)

# Managed tables: migrate everything (add, modify, drop columns)
managed_table = Table(model=Event, lifecycle=Lifecycle.managed)
await admin.migrate_table(managed_table)

# Protected tables: only add columns (no drop/modify)
protected_table = Table(model=Event, lifecycle=Lifecycle.protected)
await admin.migrate_table(protected_table)

# External tables: no migration
external_table = Table(model=Event, lifecycle=Lifecycle.external)
# Migration will be skipped, unless force=True
await admin.migrate_table(external_table, force=True)
```

### Bulk Migrations

Migrate all tables in a registry:

```py
from pyclickhouse import Client, Admin, default_registry

async def migrate_all_tables():
    client = Client()
    admin = Admin(client)
    
    async with client:
        # Migrate all tables from the default registry
        await admin.migrate_all(
            default_registry,
            database="analytics",
            force=False
        )
```

### Column-Level Modifications

Perform specific column operations:

```py
async def modify_columns():
    client = Client()
    admin = Admin(client)
    
    async with client:
        events = Table(model=Event, name="events")
        
        # Add a new column
        from pyclickhouse import Column
        new_col = Column(
            type="String",
            name="source",
            comment="Event source"
        )
        await admin.add_column(events, new_col)
        
        # Drop a column
        await admin.drop_column(events, "deprecated_field")
        
        # Modify a column
        modified_col = Column(
            type="Nullable(String)",
            name="description",
            comment="Updated description"
        )
        await admin.modify_column(events, modified_col)
```

---

## Type Mapping and Conversion

PyClickHouse automatically converts between Python and ClickHouse types. This section shows all supported type mappings and conversions.

### Python to ClickHouse Type Mapping

#### Primitive Types

| Python Type | ClickHouse Type | Example |
|---|---|---|
| `int` | `Int64` | `age: int` |
| `float` | `Float64` | `temperature: float` |
| `str` | `String` | `name: str` |
| `bool` | `Bool` | `is_active: bool` |
| `date` | `Date` | `birth_date: date` |
| `datetime` | `DateTime` | `created_at: datetime` |
| `Decimal` | `Decimal` | `amount: Decimal` |
| `UUID` | `UUID` | `id: UUID` |
| `IPv4Address` | `IPv4` | `ip: IPv4Address` |
| `IPv6Address` | `IPv6` | `ip: IPv6Address` |

#### Collection Types

| Python Type | ClickHouse Type | Example |
|---|---|---|
| `list[T]` | `Array(T)` | `tags: list[str]` → `Array(String)` |
| `tuple[T1, T2, ...]` | `Tuple(T1, T2, ...)` | `coords: tuple[float, float]` → `Tuple(Float64, Float64)` |
| `dict[K, V]` | `Map(K, V)` | `metadata: dict[str, str]` → `Map(String, String)` |

#### Special Types

| Python Type | ClickHouse Type | Example |
|---|---|---|
| `Optional[T]` or `T \| None` | `Nullable(T)` | `nickname: Optional[str]` → `Nullable(String)` |
| `Enum` | `Enum(values)` | `status: Status` → `Enum('ACTIVE', 'INACTIVE')` |
| `Literal[...]` | `Enum(values)` | `priority: Literal['low', 'high']` → `Enum('low', 'high')` |
| `dict` (untyped) | `JSON` | `metadata: dict` → `JSON` |
| `Union[T1, T2, ...]` | `Variant(T1, T2, ...)` | `data: Union[int, str]` → `Variant(Int64, String)` |

#### Nested Generic Types

| Python Expression | ClickHouse Type |
|---|---|
| `list[Optional[int]]` | `Array(Nullable(Int64))` |
| `Optional[list[str]]` | `Nullable(Array(String))` |
| `dict[str, list[int]]` | `Map(String, Array(Int64))` |
| `tuple[str, list[int], Optional[float]]` | `Tuple(String, Array(Int64), Nullable(Float64))` |

### ClickHouse to Python Type Mapping

#### Conversion During Query Results

When querying data, ClickHouse types are automatically converted to Python types:

| ClickHouse Type | Python Type | Notes |
|---|---|---|
| `Int*` (Int8, Int16, ..., Int64) | `int` | All integer variants map to Python int |
| `UInt*` (UInt8, UInt16, ..., UInt64) | `int` | Unsigned integers map to Python int |
| `Float32`, `Float64` | `float` | All float variants map to Python float |
| `Decimal(...)` | `float` | Decimal is converted to Python float |
| `String`, `FixedString(...)` | `str` | All string types map to Python str |
| `UUID` | `str` | UUID is returned as string |
| `Bool` | `bool` | ClickHouse Bool maps to Python bool |
| `Date` | `date` | ClickHouse Date maps to Python date |
| `DateTime` | `datetime` | ClickHouse DateTime maps to Python datetime |
| `Array(T)` | `list` | Arrays map to Python lists |
| `Map(K, V)` | `dict` | Maps map to Python dicts |
| `Tuple(...)` | `tuple` | Tuples map to Python tuples |
| `Enum(...)` | `str` | Enum values are returned as strings |
| `Nullable(T)` | `Optional[T]` | Nullable types can be None or T |
| `LowCardinality(T)` | `T` | LowCardinality wrapper is transparent |
| `JSON` | `Any` | JSON is returned with dynamic type |
| `Dynamic` | `Any` | Dynamic type maps to Any |

### Type Conversion Examples

#### Converting Integer Variants

```py
from pydantic import BaseModel
from pyclickhouse import Table

class Metrics(BaseModel):
    small_count: int      # Int64 (all ints use Int64)
    big_number: int       # Int64
    flag: bool            # Bool (distinct type)

metrics = Table(model=Metrics)

# All integer fields become Int64 in ClickHouse
# Query results convert back to Python int
```

#### Converting Nullable Types

```py
from typing import Optional
from pydantic import BaseModel
from pyclickhouse import Table

class User(BaseModel):
    id: int
    nickname: Optional[str] = None
    age: Optional[int] = None

users = Table(model=User)

# Query result conversions:
# id: int (non-null)
# nickname: Optional[str] (can be None)
# age: Optional[int] (can be None)
```

#### Converting Collection Types

```py
from typing import List, Dict, Tuple
from pydantic import BaseModel
from pyclickhouse import Table

class Document(BaseModel):
    id: int
    tags: List[str]
    scores: List[float]
    metadata: Dict[str, str]
    location: Tuple[float, float]

documents = Table(model=Document)

# Query result conversions:
# tags: list of strings
# scores: list of floats
# metadata: dict with string keys and values
# location: tuple of two floats
```

### Type Conversion Best Practices

#### Use Explicit Types

```py
# Good: explicit types
class Event(BaseModel):
    id: int
    timestamp: str
    value: float
    tags: list[str]

# Avoid: using Any
from typing import Any
class WeakEvent(BaseModel):
    data: Any  # Results in Dynamic type
```

#### Use Optional for Nullable Columns

```py
from typing import Optional

# Good: explicitly nullable
class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# Columns will be: id Int64, name String, description Nullable(String)
```

#### Use Proper Date/DateTime Types

```py
from datetime import date, datetime

# Good: specific temporal types
class Event(BaseModel):
    event_date: date
    created_at: datetime
    processed_at: str  # If you need string format

# Avoid: storing dates as strings unnecessarily
class WeakEvent(BaseModel):
    date: str  # Better as date type
```

#### Define Enums for Limited Values

```py
from enum import StrEnum, auto

# Good: enum for status field
class OrderStatus(StrEnum):
    PENDING = auto()
    PROCESSING = auto()
    COMPLETED = auto()

class Order(BaseModel):
    id: int
    status: OrderStatus

# Avoid: string for limited values
class WeakOrder(BaseModel):
    status: str  # Better as Enum
```

---

## Complete Example

Here's a complete example showing table creation, migration, and usage:

```py
from typing import Annotated, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pyclickhouse import (
    Client, Table, Query, F, Admin, Writer, Reader,
    Column, engines, Lifecycle, default_registry
)

# Define a Pydantic model with customized columns
class Event(BaseModel):
    timestamp: Annotated[str, Column(
        comment="Event timestamp",
        ttl_expression="timestamp + INTERVAL 30 DAY"
    )] = Field(description="When the event occurred")
    event_id: int
    event_name: Annotated[str, Column(comment="Name of the event")]
    user_id: int
    value: Annotated[float, Column(comment="Event value")]
    tags: Annotated[list[str], Column(comment="Event tags")]
    metadata: Optional[dict] = None

# Create a table with custom configuration
# (automatically registered with default_registry)
events = Table(
    model=Event,
    name="events",
    engine=engines.MergeTree(
        order_by="(user_id, timestamp)",
        partition_by="toYYYYMM(timestamp)"
    ),
    comment="Application events",
    lifecycle=Lifecycle.managed
)

async def main():
    client = Client()
    
    async with client:
        admin = Admin(client)
        
        # Create the table
        await admin.create_table(events)
        print(f"Created table: {events.get_name()}")
        
        # Get table info
        print(f"Table name: {events.get_name()}")
        print(f"Model: {events.get_model()}")
        print(f"Engine: {events.get_engine()}")
        print(f"Lifecycle: {events.get_lifecycle()}")
        
        # Get columns
        print("\nColumns:")
        for col_name, col in events.get_columns().items():
            print(f"  {col_name}: {col.type} - {col.comment}")
        
        # Insert data
        print("\nInserting data...")
        async with Writer(client, events) as writer:
            for i in range(1000):
                event = Event(
                    timestamp="2024-01-15",
                    event_id=i,
                    event_name=["click", "view", "purchase"][i % 3],
                    user_id=i % 100,
                    value=float(i % 50),
                    tags=["tag1", "tag2"] if i % 2 == 0 else ["tag3"],
                    metadata={"source": "api"} if i % 5 == 0 else None
                )
                await writer.insert(event)
        
        # Query with expressions and filters
        print("\nQuerying with filters...")
        query = Query(events).filter(
            (events.value > 10) & 
            (events.event_name == "click")
        ).aggregate(
            count=F.count(),
            total_value=F.sum(events.value)
        )
        
        reader = Reader(client, query)
        results = await reader.query()
        
        for result in results:
            print(f"Click events: {result['count']}, Total: {result['total_value']}")
        
        # Stream high-value events
        print("\nStreaming high-value events...")
        stream_query = Query(events).filter(
            events.value > 20
        ).sort(-events.value).take(100)
        
        stream_reader = Reader(client, stream_query, model=Event)
        results = await stream_reader.stream()
        
        print("Top high-value events:")
        async for event in results:
            print(f"  {event.event_name}: {event.value}")
        
        # Reflect an existing table
        print("\nReflecting table structure...")
        reflected_table = await admin.get_table("events")
        print(f"Reflected table: {reflected_table.get_name()}")
        print(f"Reflected columns: {list(reflected_table.get_columns().keys())}")
        
        # Migrate table (if schema changed)
        print("\nMigrating table...")
        was_migrated = await admin.migrate_table(events)
        print(f"Table migration completed: {was_migrated}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

---

Learn more about the [Table API](/references/table), [Query Builder](/concepts/query), [Admin](/concepts/admin), [Reader](/concepts/reader), and [Writer](/concepts/writer).