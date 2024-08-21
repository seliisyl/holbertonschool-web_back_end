#!/usr/bin/env python3
"""
Module 2-hypermedia_pagination
Contains Server class for pagination with hypermedia support.
"""

import csv
from math import ceil
from typing import List, Dict, Tuple, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate start and end indexes for pagination."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of the dataset.

        Args:
            page (int): The page number. Must be > 0.
            page_size (int): The number of items per page. Must be > 0.

        Returns:
            List[List]: A list of rows for the requested page.
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"

        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()

        return (
            dataset[start_idx:end_idx]
            if start_idx < len(dataset)
            else []
        )

    def get_hyper(
        self, page: int = 1, page_size: int = 10
    ) -> Dict[str, Optional[int]]:
        """
        Retrieve a page with pagination metadata.

        Args:
            page (int): The page number. Must be > 0.
            page_size (int): The number of items per page. Must be > 0.

        Returns:
            Dict: A dictionary containing pagination details.
        """
        data = self.get_page(page, page_size)
        total_pages = ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
