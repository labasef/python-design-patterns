from asyncio import TimeoutError, Event, run
from asyncio.tasks import create_task, gather, sleep, wait_for
from asyncio.queues import Queue
from collections.abc import AsyncIterator, Callable
from random import random


class Business:
    @staticmethod
    async def producer_logic_str(data: str) -> AsyncIterator[str]:
        """
        Async generator that yields characters from a string with random delays.
        """
        for char in data:
            await sleep(random())
            yield char

    @staticmethod
    async def producer_logic_numbers(data: int) -> AsyncIterator[int]:
        """
        Async generator that yields numbers from a range with random delays.
        """
        for num in range(data):
            await sleep(random())
            yield num

    @staticmethod
    async def consumer_logic(data, multiplier: int = 2) -> str:
        """
        coroutine that converts the input string to uppercase.
        showcases a simple consumer logic.
        Use in the queue_consumer function, to apply this logic to the data received from the queue.
        """
        if isinstance(data, int):
            return str(data*multiplier)
        elif isinstance(data, str):
            return data.upper()*multiplier
        else:
            return data


class QueueProducer:

        def __init__(self, queue: Queue, producer_func: Callable):
            self.queue = queue
            self.producer_func = producer_func

        async def queue_producer(self, func: Callable, *args, **kwargs) -> None:
            """
            Asynchronously put the results from an async generator into a queue.
            The func function is used to generate the data.
            Args:
            - queue: the queue to put the results into
            - func: the function to generate the data
            - args: additional positional arguments to pass to the func
            - kwargs: additional keyword arguments to pass to the func
            """
            async for result in func(*args, **kwargs):
                await self.queue.put(result)

        async def __call__(self, *args, **kwargs) -> None:
            await self.queue_producer(self.producer_func, *args, **kwargs)

class QueueConsumer:

            def __init__(self, queue: Queue, consumer_func: Callable):
                self.queue = queue
                self.stop_event = Event()
                self.consumer_func = consumer_func

            async def queue_consumer(self, func: Callable, timeout: float, *args, **kwargs) -> AsyncIterator[str]:
                """
                Asynchronously process results from a queue with a timeout.
                Args:
                - queue: the queue to consume from
                - func: the function process the data received from the queue
                - timeout: the max time to wait for the next item in the queue
                - stop_event: an event to signal the consumer to stop
                - args: additional positional arguments to pass to the func
                - kwargs: additional keyword arguments to pass to the func
                """
                while not self.stop_event.is_set():
                    try:
                        res = await wait_for(self.queue.get(), timeout)
                        yield await func(res, *args, **kwargs)
                    except TimeoutError:
                        break

            async def __call__(self, timeout: float = 5.0, *args, **kwargs) -> AsyncIterator[str]:
                # Iterate through the consumer until it times out:
                async for result in self.queue_consumer(self.consumer_func, timeout=timeout, *args, **kwargs):
                    yield result
                    if random() < 0.1:
                        yield "Consumer is taking a break..."
                        await sleep(1)
                    if random() > 0.95:
                        yield "Consumer is cancelled!"
                        # Signal the producer tasks to stop:
                        self.stop_event.set()
                print("All producers are done.")

async def main():
    q = Queue()

    dataset = ["abc", "xyz", "foo"]
    producers = [
        create_task(QueueProducer(q, Business.producer_logic_str)(data))
        for data in dataset
    ]
    producers.extend([
        create_task(QueueProducer(q, Business.producer_logic_numbers)(3))
    ])
    consumer = QueueConsumer(q, Business.consumer_logic)
    async for result in consumer(multiplier=3):
        print(result)
    await gather(*producers)  # Clean up the producer tasks

if __name__ == '__main__':
    run(main())