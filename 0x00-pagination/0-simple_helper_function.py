#!/usr/bin/env python3
"""
This module contains the function `index_range`.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    index_range takes in a page number and the page size, and returns a tuple
    of the starting index and end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    if not all(isinstance(i, int) for i in (page, page_size)):
        raise TypeError("page and page_size must be integers")
    if page < 1 or page_size < 1:
        raise ValueError("page and page_size must be positive integers")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)

    try:
        should_err = index_range("not an int", 0)
    except TypeError:
        print("TypeError when page/page_size is less than 1")

    try:
        should_err = index_range(1, 0)
    except ValueError:
        print("ValueError when page/page_size is less than 1")
