---
title: Reader
---

The `Reader` class executes queries against ClickHouse and returns results with optional Pydantic model validation. It supports both eager evaluation (loading all results at once) and streaming (for large result sets).

---

## Creating a Reader

### From a Table

Create a reader from a table definition:

```py
from pyclickhouse import Reader, Client, Table
from pydantic import BaseModel

class Event(BaseModel):
    id: int
    name: str
    value: float

events = Table(model=Event, name="events")

client = Client()

async with client:
    reader = Reader(client, events)
    results = await reader.query()
```

### From a Query

Use a `Query` builder result:

```py
from pyclickhouse import Query

query = Query(events).filter(events.value > 10)

async with client:
    reader = Reader(client, query)
    results = await reader.query()
```

### From Raw SQL

Pass a raw SQL string:

```py
async with client:
    reader = Reader(client, "SELECT * FROM events WHERE id > 10")
    results = await reader.query()
```

### With Result Model Validation

Automatically validate results against a Pydantic model:

```py
async with client:
    reader = Reader(client, events, model=Event)
    results = await reader.query()
    
    for result in results:
        # Each result is an Event instance
        print(result.name, result.value)
```

### With Parameter Model

Define a Pydantic model for query parameter validation. Pass the model class (not an instance) when creating the Reader:

```py
from pydantic import BaseModel

class EventFilter(BaseModel):
    min_value: float
    max_value: float

async with client:
    # Pass the class, not an instance
    reader = Reader(
        client,
        "SELECT * FROM events WHERE value BETWEEN {min_value:Float32} AND {max_value:Float32}",
        parameters=EventFilter
    )
```

---

## Query Execution

### Load All Results at Once

Use `query()` to execute and return all results as a list:

```py
async with client:
    reader = Reader(client, events)
    results = await reader.query()
    
    print(f"Got {len(results)} results")
    for event in results:
        print(event)
```

---

## Parameter Handling

Parameters passed to `query()` or `stream()` can be either:
- A `dict[str, Any]` - raw dictionary with parameter values
- A Pydantic model instance - already validated model instance

### Using Dictionary Parameters

Pass parameters as a simple dictionary:

```py
async with client:
    reader = Reader(
        client,
        "SELECT * FROM events WHERE value > {min_val:Float32}"
    )
    # Pass dict with parameter values
    results = await reader.query(
        parameters={"min_val": 10.0}
    )
```

### Using Pydantic Model Instance

Pass an already-instantiated Pydantic model as parameters:

```py
class EventFilter(BaseModel):
    min_value: float

async with client:
    reader = Reader(
        client,
        "SELECT * FROM events WHERE value > {min_value:Float32}"
    )
    # Pass a model instance
    results = await reader.query(
        parameters=EventFilter(min_value=10.0)
    )
```

---

## Parameter Validation

### Without Parameter Model

If no parameter model was specified in Reader, parameters are used as-is:

```py
async with client:
    reader = Reader(
        client,
        "SELECT * FROM events WHERE value > {min_val:Float32}"
    )
    
    # Both dict and model instance work - no validation
    results = await reader.query(parameters={"min_val": 10.0})
    
    # Or pass a model instance
    class Filter(BaseModel):
        min_val: float
    
    results = await reader.query(parameters=Filter(min_val=20.0))
```

### With Parameter Model

When a parameter model class is specified in Reader, parameters are validated against it:

```py
class EventFilter(BaseModel):
    min_value: float
    max_value: float

async with client:
    reader = Reader(
        client,
        "SELECT * FROM events WHERE value BETWEEN {min_value:Float32} AND {max_value:Float32}",
        parameters=EventFilter  # Specify model class
    )
    
    # Option 1: Pass a dict - validated as EventFilter
    results = await reader.query(
        parameters={"min_value": 10.0, "max_value": 100.0}
    )
    
    # Option 2: Pass a model instance - must be EventFilter
    results = await reader.query(
        parameters=EventFilter(min_value=10.0, max_value=100.0)
    )
    
    # Option 3: Wrong type - raises TypeError
    class WrongFilter(BaseModel):
        min_value: float
    
    try:
        results = await reader.query(
            parameters=WrongFilter(min_value=10.0)  # TypeError!
        )
    except TypeError as e:
        print(f"Wrong model type: {e}")
```

---

## Streaming Results

### Stream Large Result Sets

Use `stream()` to iterate over results without loading everything into memory. Results from `stream()` are iterated using `async for`:

```py
async with client:
    reader = Reader(client, events, model=Event)
    results = await reader.stream()
    
    async for event in results:
        print(event)
```

### Stream with Dictionary Parameters

```py
async with client:
    reader = Reader(client, events, model=Event)
    results = await reader.stream(
        parameters={"min_value": 10.0}
    )
    
    async for event in results:
        process(event)
```

### Stream with Parameter Model

```py
class EventFilter(BaseModel):
    min_value: float

async with client:
    reader = Reader(
        client,
        events,
        model=Event,
        parameters=EventFilter
    )
    
    # Pass dict - validated as EventFilter
    results = await reader.stream(
        parameters={"min_value": 10.0}
    )
    
    async for event in results:
        process(event)
```

Or pass a model instance:

```py
async with client:
    reader = Reader(
        client,
        events,
        model=Event,
        parameters=EventFilter
    )
    
    # Pass model instance - must be EventFilter
    results = await reader.stream(
        parameters=EventFilter(min_value=10.0)
    )
    
    async for event in results:
        process(event)
```

### Configure Block Size

Control the amount of data loaded at once when streaming:

```py
async with client:
    reader = Reader(
        client,
        events,
        model=Event,
        max_block_size=100000  # Larger blocks = more memory
    )
    results = await reader.stream()
    
    async for event in results:
        print(event)
```

---

## Result Model Validation

### Automatic Deserialization

Reader automatically validates and deserializes rows:

```py
class Event(BaseModel):
    id: int
    name: str
    timestamp: str
    value: float

async with client:
    reader = Reader(client, "SELECT * FROM events", model=Event)
    results = await reader.query()
    
    # All results are Event instances
    for event in results:
        assert isinstance(event, Event)
        print(f"Event {event.id}: {event.name}")
```

### Without Model Validation

Get raw dictionaries without validation:

```py
async with client:
    reader = Reader(client, "SELECT * FROM events")
    results = await reader.query()
    
    for row in results:
        # row is a dict
        print(row["id"], row["name"])
```

---

## Advanced Configuration

### Custom Settings

Pass ClickHouse-specific settings:

```py
async with client:
    reader = Reader(
        client,
        events,
        model=Event,
        settings={
            "max_rows_to_read": 1000000,
            "read_overflow_mode": "throw",
            "max_execution_time": 300
        }
    )
```

### Transport Settings

Configure transport behavior:

```py
async with client:
    reader = Reader(
        client,
        events,
        model=Event,
        transport_settings={
            "connection_timeout": 10,
            "max_retries": 3
        }
    )
```

---

## Progress Tracking

### Monitor Rows Read During Streaming

Track the number of rows read:

```py
async with client:
    reader = Reader(client, events, model=Event)
    results = await reader.stream()
    
    async for event in results:
        if reader.read_rows % 1000 == 0:
            print(f"Read {reader.read_rows} rows...")
```

---

## Common Patterns

### Filter and Count

```py
from pyclickhouse import Query

async with client:
    query = Query(events).filter(events.value > 50)
    reader = Reader(client, query)
    results = await reader.query()
    
    print(f"Found {len(results)} high-value events")
```

### Aggregate Data

```py
from pyclickhouse import Query, F

async with client:
    query = Query(events).group(events.name).aggregate(
        total=F.sum(events.value),
        count=F.count()
    )
    reader = Reader(client, query)
    results = await reader.query()
    
    for result in results:
        print(f"{result['name']}: {result['total']} ({result['count']} events)")
```

### Process Large Result Set in Batches

```py
async with client:
    reader = Reader(client, events, model=Event)
    results = await reader.stream()
    
    batch = []
    async for event in results:
        batch.append(event)
        
        if len(batch) >= 100:
            await process_batch(batch)
            batch = []
    
    # Process remaining
    if batch:
        await process_batch(batch)
```

### Stream with Filter Parameters

```py
async with client:
    query = Query(events).filter(
        (events.timestamp >= "{start_date:String}") & 
        (events.timestamp <= "{end_date:String}")
    )
    
    reader = Reader(
        client,
        query,
        model=Event,
        parameters=DateRange
    )
    
    results = await reader.query(
        parameters=DateRange(start_date="2024-01-01", end_date="2024-01-31")
    )
    
    for event in results:
        print(event)
```

### Multiple Readers in Parallel

```py
import asyncio

async with client:
    reader1 = Reader(client, users, model=User)
    reader2 = Reader(client, events, model=Event)
    
    users_results, events_results = await asyncio.gather(
        reader1.query(),
        reader2.query()
    )
```

---

## Error Handling

### Handle Query Errors

```py
from clickhouse_connect.exc import ClickHouseException

async with client:
    reader = Reader(client, "SELECT * FROM nonexistent")
    try:
        results = await reader.query()
    except ClickHouseException as e:
        print(f"Query failed: {e}")
```

### Handle Parameter Validation Errors

```py
from pydantic import ValidationError

class EventFilter(BaseModel):
    min_value: float

async with client:
    reader = Reader(
        client,
        "SELECT * FROM events WHERE value > {min_value:Float32}",
        parameters=EventFilter
    )
    
    try:
        # This dict is missing required field - validation fails
        results = await reader.query(
            parameters={"invalid_field": 10.0}
        )
    except (ValidationError, TypeError) as e:
        print(f"Invalid parameters: {e}")
```

### Handle Result Validation Errors

```py
from pydantic import ValidationError

async with client:
    reader = Reader(client, "SELECT * FROM events", model=Event)
    try:
        results = await reader.query()
    except ValidationError as e:
        print(f"Result validation failed: {e}")
```

### Handle Streaming Errors

```py
from clickhouse_connect.exc import ClickHouseException

async with client:
    reader = Reader(client, events, model=Event)
    try:
        results = await reader.stream()
        async for event in results:
            print(event)
    except ClickHouseException as e:
        print(f"Stream failed: {e}")
```

---

## Complete Example

Here's a complete example combining query building, parameter validation, and both query and streaming patterns:

```py
from pydantic import BaseModel
from pyclickhouse import Client, Reader, Query, Table, F

class Event(BaseModel):
    timestamp: str
    event_name: str
    value: float

class DateRange(BaseModel):
    start_date: str
    end_date: str

events = Table(model=Event, name="events")

async def analyze_events():
    client = Client()
    
    async with client:
        # Simple query - load all results
        reader = Reader(client, events, model=Event)
        all_events = await reader.query()
        print(f"Total events: {len(all_events)}")
        
        # Filtered query with parameter model
        filtered_reader = Reader(
            client,
            "SELECT * FROM events WHERE timestamp BETWEEN {start_date:String} AND {end_date:String}",
            model=Event,
            parameters=DateRange
        )
        # Parameters are validated against DateRange
        filtered = await filtered_reader.query(
            parameters=DateRange(start_date="2024-01-01", end_date="2024-12-31")
        )
        print(f"Events in 2024: {len(filtered)}")
        
        # Aggregation query
        agg_query = Query(events).group(events.event_name).aggregate(
            total=F.sum(events.value),
            count=F.count()
        )
        agg_reader = Reader(client, agg_query)
        stats = await agg_reader.query()
        
        for stat in stats:
            avg = stat['total'] / stat['count']
            print(f"{stat['event_name']}: total={stat['total']}, avg={avg:.2f}")
        
        # Stream large result set
        print("\nStreaming high-value events:")
        stream_query = Query(events).filter(events.value > 1000)
        stream_reader = Reader(
            client,
            stream_query,
            model=Event,
            max_block_size=50000
        )
        results = await stream_reader.stream()
        
        count = 0
        async for event in results:
            count += 1
            if count <= 5:
                print(f"  {event.event_name}: {event.value}")
        
        print(f"Total high-value events: {stream_reader.read_rows}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(analyze_events())
```

---

## Choosing Between query() and stream()

### Use `query()` when:
- You need all results at once
- The result set is small to medium sized
- You need to know the total count
- Random access to results is needed
- Results fit comfortably in memory

```py
# Load all results into a list
async with client:
    reader = Reader(client, Query(events).filter(events.id < 1000))
    results = await reader.query()
    print(f"Got {len(results)} results")
```

### Use `stream()` when:
- Processing large result sets
- Memory usage is a concern
- Processing rows one at a time
- Real-time processing as data arrives
- You only need to iterate once
- Processing data immediately without storing

```py
# Stream results without loading everything
async with client:
    reader = Reader(client, Query(events))
    results = await reader.stream()
    async for event in results:
        await process_event(event)
```

---

Learn more about the [Reader API](/references/reader), [Query Builder](/concepts/query), and [Tables](/concepts/table).