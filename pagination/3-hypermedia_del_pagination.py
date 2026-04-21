#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""


import csv
from typing import Any, Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache dataset from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by sorting position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: Optional[int] = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """Return deletion-resilient hypermedia pagination information."""
        if index is None:
            index = 0

        indexed_dataset = self.indexed_dataset()
        assert index >= 0 and index <= max(indexed_dataset.keys())

        data = []
        next_index = index
        max_index = max(indexed_dataset.keys())

        while len(data) < page_size and next_index <= max_index:
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
