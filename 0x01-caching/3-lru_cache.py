#!/usr/bin/env python3
"""This is the `3-lru_cache` module. It contains the class `LRUCache`.
"""

from typing import Any
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    This is the class `LRUCache`. It inherits from `BaseCaching` and
    implements a caching system.
    """

    def __init__(self):
        """Initializes a new LRUCache object.
        """
        super().__init__()
        self.queue = []

    def put(self, key: Any, item: Any) -> None:
        """`put` adds the `item` with given `key` in the cache.
        """
        if key is None or item is None:
            return

        if BaseCaching.MAX_ITEMS <= 0:
            print("Could not insert [{}:{}] as cache max size is <= 0")

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = None
            if len(self.queue) > 0:
                lru_key = self.queue.pop(0)

            if key not in self.cache_data.keys() and lru_key:
                try:
                    del self.cache_data[lru_key]
                    print("DISCARD:", lru_key)
                except KeyError:
                    msg = "Could not insert [{}:{}] as LRU key not in cache"
                    print(msg.format(key))
                    return
            elif key in self.queue:
                self.queue.remove(key)
            else:
                return

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key: Any) -> Any:
        """
        `get` gets an item by key and maintains a queue of the keys.
        """
        if key is not None and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = LRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Chee-zaram")
    my_cache.put("D", "Okeke")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
