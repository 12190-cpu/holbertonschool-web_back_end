#!/usr/bin/env python3
"""Module that defines an asynchronous function running coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times and returns the delays in ascending order.

    Args:
        n (int): The number of coroutines to run.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = []
    delays = []

    # Create n coroutines/tasks
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    # as_completed returns results in the order they finish
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays