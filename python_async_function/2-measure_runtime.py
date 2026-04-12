#!/usr/bin/env python3
"""Module that measures the runtime of an asynchronous routine."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time of wait_n.

    Args:
        n (int): The number of coroutines to run.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The total runtime divided by n.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total_time = end - start
    return total_time / n