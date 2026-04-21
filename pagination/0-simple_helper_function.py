#!/usr/bin/env python3
""" Module that provides a helper function for pagination """

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return a tuple comntaning the start index and end index for pagination. The page numbering is 1-indexed, meaning that page 1 starts at index 0. """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
