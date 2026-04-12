#!/usr/bin/env python3
"""Module that defines an asynchronous generator."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously yields 10 random floating-point numbers.

    The coroutine waits for 1 second before yielding each number.
    Each yielded number is between 0 and 10.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        # Wait asynchronously for 1 second
        await asyncio.sleep(1)

        # Yield a random float between 0 and 10
        yield random.uniform(0, 10)