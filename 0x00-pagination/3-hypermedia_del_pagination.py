#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indexes for a given pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server instance with dataset and indexed dataset as None.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        Returns:
            List[List]: The dataset loaded from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create and cache an indexed version of the dataset.

        Returns:
            Dict[int, List]: The indexed dataset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieve a page of the dataset starting from a specific index with pagination metadata.

        Args:
            index (int): The starting index of the page.
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary containing pagination metadata and the dataset page.
        """
        assert isinstance(index, int) and index >= 0, "Index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        indexed_data = self.indexed_dataset()
        data = []
        current_index = index

        for _ in range(page_size):
            while current_index in indexed_data:
                data.append(indexed_data[current_index])
                current_index += 1
                if len(data) == page_size:
                    break
            else:
                break

        next_index = current_index if current_index in indexed_data else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
