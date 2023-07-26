#!/usr/bin/env python3
""" BasicCache module.
"""
from typing import Any
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class used as a caching system.
    """

    def put(self, key: Any, item: Any) -> None:
        """ `put` adds the `item` with given `key` in the cache.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """ `get` gets an item by key.
        """
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Chee-zaram")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
