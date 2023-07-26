#!/usr/bin/env python3
"""This is the `2-lifo_cache` module. It contains the class `LIFOCache`.
"""

from typing import Any
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    This is the class `LIFOCache`. It inherits from `BaseCaching` and
    implements a caching system which uses the LIFO algorithm, removing the
    last item inserted into the cache when the cache is full.
    """

    def __init__(self):
        """Initializes a new FIFOCache object.
        """
        super().__init__()
        self.queue = []

    def put(self, key: Any, item: Any) -> None:
        """
        `put` adds the `item` with given `key` in the cache. If the cache is
        full, it removes the last item inserted into the cache to make room
        for the new item.
        If the item already exists, it is replaced by the new item, and it
        becomes the last item inserted into the cache.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                last_key = self.queue.pop()
                del self.cache_data[last_key]
                print("DISCARD:", last_key)
            else:
                self.queue.remove(key)

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key: Any) -> Any:
        """`get` gets an item by key.
        """
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = LIFOCache()
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
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
