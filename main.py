import asyncio
import time
import random

async def simulate_query(item_id: int):
    """
    Simulates a Query operation: fetching data once.
    Queries are typically idempotent and don't change server state.
    """
    print(f"[{time.strftime('%H:%M:%S')}] Querying data for item_id: {item_id}...")
    await asyncio.sleep(random.uniform(0.5, 1.5)) # Simulate network delay
    data = {"id": item_id, "name": f"Item {item_id}", "status": "active"}
    print(f"[{time.strftime('%H:%M:%S')}] Query result for item {item_id}: {data}")
    return data

async def simulate_mutation(item_id: int, new_status: str):
    """
    Simulates a Mutation operation: changing server-side data.
    Mutations are typically not idempotent and alter state.
    """
    print(f"[{time.strftime('%H:%M:%S')}] Mutating item {item_id} to status: {new_status}...")
    await asyncio.sleep(random.uniform(1.0, 2.0)) # Simulate network delay and processing
    # In a real scenario, this would update a database or external service
    updated_data = {"id": item_id, "name": f"Item {item_id}", "status": new_status, "updated_at": time.time()}
    print(f"[{time.strftime('%H:%M:%S')}] Mutation successful for item {item_id}. New state: {updated_data['status']}")
    return updated_data

async def simulate_stream(item_id: int):
    """
    Simulates a Stream operation: continuous flow of data updates.
    Streams push data from server to client over time.
    """
    print(f"[{time.strftime('%H:%M:%S')}] Starting stream for item {item_id}...")
    for i in range(1, 6): # Yield 5 updates
        await asyncio.sleep(random.uniform(0.3, 0.8)) # Simulate delay between updates
        update_type = random.choice(["price_change", "status_update", "stock_level"])
        value = random.randint(10, 100) if update_type == "price_change" else random.choice(["available", "low_stock"])
        yield {"item_id": item_id, "update_type": update_type, "value": value, "timestamp": time.time()}
        print(f"[{time.strftime('%H:%M:%S')}] Stream update for item {item_id} ({i}/5)")
    print(f"[{time.strftime('%H:%M:%S')}] Stream for item {item_id} ended.")

async def main():
    print("--- Demonstrating Asynchronous Workloads: Query, Mutation, Stream ---")

    # 1. Query Example
    print("\n--- Query Example (fetching data) ---")
    item_data = await simulate_query(101)
    print(f"Main received queried data: {item_data}")

    # 2. Mutation Example
    print("\n--- Mutation Example (changing data) ---")
    updated_item = await simulate_mutation(101, "inactive")
    print(f"Main received mutated data confirmation: {updated_item}")

    # 3. Stream Example
    print("\n--- Stream Example (continuous data flow) ---")
    async for update in simulate_stream(202):
        print(f"Main received stream update: {update}")
        # In a real application, you would process this update (e.g., update UI)

    print("\n--- All asynchronous operations completed ---")

if __name__ == "__main__":
    asyncio.run(main())
