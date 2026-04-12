#!/usr/bin/env python3
"""Module that defines an asynchronous function using asyncio Tasks."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times and returns the delays in ascending order.

    Args:
        n (int): The number of tasks to run.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = []
    delays = []

    # Create n asyncio tasks
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    # Collect results in completion order
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays