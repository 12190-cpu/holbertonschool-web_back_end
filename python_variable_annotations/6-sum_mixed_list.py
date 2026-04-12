#!/usr/bin/env python3
"""Module that provides a function to sum a list of ints and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of numbers.

    Returns:
        float: The sum of the list elements.
    """
    return float(sum(mxd_lst))