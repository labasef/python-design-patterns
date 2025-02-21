from asyncio import TimeoutError, Event, run
from asyncio.tasks import create_task, gather, sleep, wait_for
from asyncio.queues import Queue
from collections.abc import AsyncIterator
from random import random

async def producer_logic(data: str) -> AsyncIterator[str]:
    """
    Ansync generator that yields characters from a string with random delays.
    """
    for char in data:
        await sleep(random())
        try:
            if random() < 0.3:
                raise ValueError("Producer failed!")
            yield char
        except ValueError as e:
            # yield the error to the queue producer
            yield e

async def consumer_logic(data: str):
    """
    coroutine that converts the input string to uppercase.
    showcases a simple consumer logic.
    Use in the queue_consumer function, to apply this logic to the data received from the queue.
    """
    return data.upper()

async def queue_producer(queue: Queue[str], data: str) -> None:
    """
    Asynchronously put the results from an async generator into a queue.
    The producer_logic function is used to generate the data.
    """
    async for result in producer_logic(data):
        # Check if the result is an exception
        if isinstance(result, Exception):
            print(f"Producer failed: {result}")
        else:
            await queue.put(result)

async def queue_consumer(queue: Queue[str], timeout: float, stop_event: Event) -> AsyncIterator[str]:
    """
    Asynchronously process results from a queue with a timeout.
    Here we convert the results to uppercase.
    """
    while not stop_event.is_set():
        try:
            res = await wait_for(queue.get(), timeout)
            yield await consumer_logic(res)
        except TimeoutError:
            break

async def produce_consume(dataset, timeout: float = 5.0) -> AsyncIterator[str]:
    q: Queue[str] = Queue()
    # Launch the producer tasks:
    producers = [
        create_task(queue_producer(q, data))
        for data in dataset
    ]
    stop_event = Event()
    # Iterate through the consumer until it times out:
    async for result in queue_consumer(q, timeout=timeout, stop_event=stop_event):
        yield result
        if random() < 0.1:
            yield "Consumer is taking a break..."
            await sleep(1)
        if random() > 0.99:
            yield "Consumer is cancelled!"
            # Signal the producer tasks to stop:
            stop_event.set()
    await gather(*producers)  # Clean up the producer tasks
    print("All producers are done.")

async def main():
    async for result in produce_consume(["abc", "xyz", "foo"]):
        print(result)

if __name__ == '__main__':
    run(main())