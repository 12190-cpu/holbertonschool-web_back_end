#!/usr/bin/env python3
"""Module that provides a function to create a key-value tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the second element is the square of the value.

    Args:
        k (str): The key.
        v (Union[int, float]): The value to square.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value.
    """
    return (k, float(v ** 2))