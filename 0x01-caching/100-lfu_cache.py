#!/usr/bin/env python3
"""
This module contains the class `LFUCache` as a caching system.
"""

from typing import Any, Optional
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class.
    """

    def __init__(self):
        """Initializes LFUCache instances.
        """
        super().__init__()
        self.frequencies = {}
        self.min_frequency = 1
        self.queue = []

    def put(self, key: Any, item: Any) -> None:
        """
        `put` uses the LFU algorithm to insert a new item with given key
        into the cache. If the cache is full, it replaces the least frequently
        used item in the cache with the new item.
        If key or item is None, it does nothing.
        """
        if key is None or item is None:
            return

        if BaseCaching.MAX_ITEMS <= 0:
            print("Could not insert [{}:{}] as cache max size is <= 0")

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_keys = [k for k, v in self.frequencies.items() if v ==
                        self.min_frequency]
            i = 0
            lru_key = self.queue[i]
            while i < len(self.queue) - 1 and lru_key not in lfu_keys:
                i += 1
                lru_key = self.queue[i]

            if key not in self.cache_data:
                print("DISCARD:", lru_key)
                del self.cache_data[lru_key]
                del self.frequencies[lru_key]
            self.queue.remove(lru_key)

        self.cache_data[key] = item
        self.queue.append(key)
        self.update_frequency(key)

    def get(self, key: Any) -> Optional[Any]:
        """
        `get` gets an item by key and maintains the frequency of its usage.
        """

        if key is not None and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            self.update_frequency(key)

        return self.cache_data.get(key)

    def update_frequency(self, key: Any) -> None:
        """Returns the key and value of least frequently used item in cache.
        """
        value = self.frequencies.get(key)
        self.frequencies[key] = int(value) + 1 if value is not None else 1
        self.min_frequency = min(self.frequencies.values())


if __name__ == "__main__":
    my_cache = LFUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
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
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()
