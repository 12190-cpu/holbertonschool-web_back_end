#!/usr/bin/env python3
"""Module that measures the runtime of parallel async comprehensions."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures runtime.

    This coroutine launches four async_comprehension coroutines concurrently
    using asyncio.gather, then returns the total execution time.

    Returns:
        float: The total runtime in seconds.
    """
    # Save the start time
    start = time.time()

    # Run four async_comprehension coroutines in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    # Save the end time
    end = time.time()

    # Return the total elapsed time
    return end - start