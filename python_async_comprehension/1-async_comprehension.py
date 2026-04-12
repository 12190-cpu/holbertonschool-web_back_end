#!/usr/bin/env python3
"""Module that defines an asynchronous comprehension coroutine."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from an async generator.

    This coroutine uses an asynchronous comprehension over
    async_generator and returns the resulting list.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [number async for number in async_generator()]