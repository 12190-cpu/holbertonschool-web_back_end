#!/usr/bin/env python3
"""Module that provides a function to compute element lengths."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each element and its length.

    Args:
        lst (Iterable[Sequence]): A collection of sequences.

    Returns:
        List[Tuple[Sequence, int]]: List of tuples (element, length).
    """
    return [(i, len(i)) for i in lst]