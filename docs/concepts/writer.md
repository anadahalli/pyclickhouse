---
title: Writer
---

The `Writer` class provides efficient batch insertion of validated data into ClickHouse tables. It takes already-validated Pydantic model instances, batches them, and inserts them efficiently into the database.

---

## Creating a Writer

Create a writer with a client and table definition:

```py
from pydantic import BaseModel
from pyclickhouse import Client, Table, Writer

class User(BaseModel):
    id: int
    name: str
    email: str

users = Table(model=User, name="users")

client = Client()

async with client:
    writer = Writer(client, users)
    # ready to insert data
```

---

## Basic Usage

### Insert Single Records

The Writer accepts already-validated Pydantic model instances:

```py
async with client:
    writer = Writer(client, users)
    
    # Create a valid User instance
    user = User(id=1, name="Alice", email="alice@example.com")
    await writer.insert(user)
```

### Insert Multiple Records

Insert multiple records in a single call:

```py
async with client:
    writer = Writer(client, users)
    
    users_data = [
        User(id=1, name="Alice", email="alice@example.com"),
        User(id=2, name="Bob", email="bob@example.com"),
        User(id=3, name="Charlie", email="charlie@example.com"),
    ]
    
    for user in users_data:
        await writer.insert(user)
```

Or all at once:

```py
async with client:
    writer = Writer(client, users)
    
    await writer.insert(
        User(id=1, name="Alice", email="alice@example.com"),
        User(id=2, name="Bob", email="bob@example.com"),
        User(id=3, name="Charlie", email="charlie@example.com"),
    )
```

---

## Validation Before Insertion

Validation happens when you create the model instance, not when inserting:

```py
from pydantic import ValidationError

async with client:
    writer = Writer(client, users)
    
    # Validation happens here during model creation
    try:
        user = User(id="invalid", name="Alice", email="alice@example.com")
    except ValidationError as e:
        print(f"Invalid user: {e}")
    
    # Only valid instances reach the writer
    user = User(id=1, name="Alice", email="alice@example.com")
    await writer.insert(user)
```

### Type Checking

The Writer enforces type checking - you must pass instances of the correct model:

```py
async with client:
    writer = Writer(client, users)
    
    # This works - valid User instance
    user = User(id=1, name="Alice", email="alice@example.com")
    await writer.insert(user)
    
    # This raises TypeError - dict is not a User instance
    invalid = {"id": 1, "name": "Bob"}
    await writer.insert(invalid)  # TypeError!
```

---

## Batching

### Automatic Batching (Default)

By default, the writer batches inserts for efficiency:

```py
async with client:
    writer = Writer(client, users, batch=True, batch_size=1000)
    
    # Records are queued and automatically flushed when batch_size is reached
    for i in range(5000):
        user = User(id=i, name=f"User {i}", email=f"user{i}@example.com")
        await writer.insert(user)
    
    # Any remaining records are flushed on context manager exit
```

### Configure Batch Size

Adjust the batch size based on your needs:

```py
async with client:
    # Larger batches = better performance but more memory
    writer = Writer(client, users, batch_size=5000)
    
    for user in users_data:
        await writer.insert(user)
```

### Disable Batching

Insert immediately without batching:

```py
async with client:
    writer = Writer(client, users, batch=False)
    
    # Each insert is sent immediately to the database
    await writer.insert(user)
```

---

## Context Manager Usage

### Automatic Flush

Use the writer as an async context manager to automatically flush remaining records:

```py
async with client:
    async with Writer(client, users) as writer:
        for user in users_data:
            await writer.insert(user)
    # Remaining records are automatically flushed on exit
```

### Manual Flush

Manually flush the queue when needed:

```py
async with client:
    writer = Writer(client, users)
    
    for user in users_data:
        await writer.insert(user)
    
    # Flush remaining records
    await writer.flush()
```

---

## Progress Tracking

### Monitor Written Records

Track how many records have been written:

```py
async with client:
    async with Writer(client, users) as writer:
        for user in users_data:
            await writer.insert(user)
            print(f"Written: {writer.written_rows}")
```

### Check Queue Size

Check how many records are queued but not yet written:

```py
async with client:
    writer = Writer(client, users, batch_size=1000)
    
    for i, user in enumerate(users_data):
        await writer.insert(user)
        
        if writer.queue_size == 500:
            print(f"Queue has 500 records after inserting {i+1} users")
```

---

## Configuration

### Specify Database

Insert into a different database:

```py
async with client:
    writer = Writer(client, users, database="analytics")
    await writer.insert(user)
```

### Custom Settings

Pass ClickHouse-specific settings for the insert:

```py
async with client:
    writer = Writer(
        client,
        users,
        settings={
            "insert_quorum": 2,
            "insert_quorum_parallel": True
        }
    )
    await writer.insert(user)
```

### Transport Settings

Configure transport behavior:

```py
async with client:
    writer = Writer(
        client,
        users,
        transport_settings={
            "connection_timeout": 10,
            "max_retries": 3
        }
    )
    await writer.insert(user)
```

---

## Common Patterns

### Insert from List

```py
users_list = [
    User(id=1, name="Alice", email="alice@example.com"),
    User(id=2, name="Bob", email="bob@example.com"),
]

async with client:
    async with Writer(client, users) as writer:
        for user in users_list:
            await writer.insert(user)
```

### Insert from Generator

```py
def user_generator():
    for i in range(10000):
        yield User(id=i, name=f"User {i}", email=f"user{i}@example.com")

async with client:
    async with Writer(client, users) as writer:
        for user in user_generator():
            await writer.insert(user)
```

### Batch Insert with Progress

```py
async with client:
    async with Writer(client, users, batch_size=1000) as writer:
        for i, user in enumerate(users_data):
            await writer.insert(user)
            
            if (i + 1) % 5000 == 0:
                print(f"Progress: {i + 1}/{len(users_data)} ({writer.written_rows} written)")
```

### Insert Multiple Tables

```py
async with client:
    users_writer = Writer(client, users)
    events_writer = Writer(client, events)
    
    async with users_writer, events_writer:
        for user in users_data:
            await users_writer.insert(user)
        
        for event in events_data:
            await events_writer.insert(event)
```

### Conditional Batching

```py
async with client:
    # Use smaller batches for real-time data
    if is_real_time:
        writer = Writer(client, events, batch_size=100)
    else:
        # Use larger batches for bulk import
        writer = Writer(client, events, batch_size=10000)
    
    async with writer:
        for event in events_data:
            await writer.insert(event)
```

---

## Error Handling

### Handle Insert Errors

```py
from clickhouse_connect.exc import ClickHouseException

async with client:
    async with Writer(client, users) as writer:
        try:
            for user in users_data:
                await writer.insert(user)
        except ClickHouseException as e:
            print(f"Insert failed: {e}")
            # Remaining records in queue can be retried
```

### Handle Type Errors

```py
async with client:
    async with Writer(client, users) as writer:
        for user_data in users_data:
            try:
                user = User(**user_data)  # Validate when creating model
                await writer.insert(user)
            except (ValidationError, TypeError) as e:
                print(f"Invalid user {user_data}: {e}")
                continue  # Skip invalid records
```

---

## Performance Considerations

### Batch Size Impact

```py
# Small batches - more database roundtrips, slower
writer = Writer(client, users, batch_size=100)

# Medium batches - balanced
writer = Writer(client, users, batch_size=1000)

# Large batches - fewer roundtrips, more memory
writer = Writer(client, users, batch_size=10000)
```

### Disable Batching for Real-Time Inserts

```py
# Real-time inserts without batching
real_time_writer = Writer(client, events, batch=False)

# Batch inserts for bulk operations
bulk_writer = Writer(client, events, batch=True, batch_size=5000)
```

---

## Complete Example

Here's a complete example combining multiple Writer features:

```py
from pydantic import BaseModel, ValidationError
from pyclickhouse import Client, Table, Writer
import asyncio

class Event(BaseModel):
    timestamp: str
    event_name: str
    user_id: int
    value: float

class User(BaseModel):
    id: int
    name: str
    email: str

async def bulk_import():
    client = Client()
    
    events = Table(model=Event, name="events")
    users = Table(model=User, name="users")
    
    async with client:
        # Insert users with default batch size
        async with Writer(client, users) as user_writer:
            for i in range(1000):
                user = User(
                    id=i,
                    name=f"User {i}",
                    email=f"user{i}@example.com"
                )
                await user_writer.insert(user)
            print(f"Users written: {user_writer.written_rows}")
        
        # Insert events with larger batch size for performance
        async with Writer(client, events, batch_size=5000) as event_writer:
            for i in range(100000):
                event = Event(
                    timestamp=f"2024-01-{(i % 30) + 1:02d}",
                    event_name=["click", "view", "purchase"][i % 3],
                    user_id=i % 1000,
                    value=float(i % 100) / 10
                )
                await event_writer.insert(event)
            
            print(f"Events written: {event_writer.written_rows}")

async def streaming_insert():
    """Real-time inserts without batching"""
    client = Client()
    events = Table(model=Event, name="events")
    
    async with client:
        # Real-time mode - insert immediately
        writer = Writer(client, events, batch=False)
        
        # Simulate event stream
        for i in range(100):
            event = Event(
                timestamp="2024-01-15",
                event_name="click",
                user_id=i % 10,
                value=float(i)
            )
            await writer.insert(event)

if __name__ == "__main__":
    asyncio.run(bulk_import())
    asyncio.run(streaming_insert())
```

---

Learn more about the [Writer API](/references/writer), [Tables](/concepts/table), and [Admin](/concepts/admin).