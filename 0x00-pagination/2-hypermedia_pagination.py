#!/usr/bin/env python3
"""
This module contains the functions and classes for pagination operations.

`index_range`: function
`Server`: class
"""
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    index_range takes in a page number and the page size, and returns a tuple
    of the starting index and end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    assert all(isinstance(i, int) for i in (page, page_size))
    assert page >= 1 and page_size >= 1

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes a new Server object.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.
        """
        if self.__dataset is not None:
            return self.__dataset

        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get_page gets the dataset corresponding to the page from the database.
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()
        total_rows = len(dataset)

        if start_idx >= total_rows or end_idx >= total_rows:
            return []

        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        get_hyper returns a dictionary with the data for a dataset.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        page_size = len(data) if page_size > len(data) else page_size
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }


if __name__ == "__main__":
    server = Server()

    try:
        should_err = server.get_page(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_page(0, 0)
    except AssertionError:
        print("AssertionError raised with 0 values")

    try:
        should_err = server.get_page(1, "Chee")
    except AssertionError:
        print("AssertionError raised when page/page_size is not an int")

    print(server.get_page(1, 3))
    print(server.get_page(3, 2))
    print(server.get_page(3000, 100))
    print(server.get_hyper(1, 2))
    print()

    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
