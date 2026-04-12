#!/usr/bin/env python3
"""Module that provides a function to sum a list of floats."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of the list elements.
    """
    return sum(input_list)