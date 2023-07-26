#!/usr/bin/env python3
"""This is the `1-fifo_cache` module. It contains the class `FIFOCache`.
"""

from typing import Any
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This is the class `FIFOCache`. It inherits from `BaseCaching` and
    implements a caching system.
    """

    def __init__(self):
        """Initializes a new FIFOCache object.
        """
        super().__init__()
        self.queue = []

    def put(self, key: Any, item: Any) -> None:
        """`put` adds the `item` with given `key` in the cache.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.queue.pop(0)
            assert first_key in self.cache_data, "Could not find first key."
            del self.cache_data[first_key]
            print("DISCARD:", first_key)

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key: Any) -> Any:
        """`get` gets an item by key.
        """
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Chee-zaram")
    my_cache.put("D", "Okeke")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
