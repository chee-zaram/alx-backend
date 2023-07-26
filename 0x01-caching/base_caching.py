#!/usr/bin/python3
""" BaseCaching module.
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initializes a BaseCaching object.
        """
        self.cache_data = {}

    def print_cache(self):
        """ `print_cache` prints the cache.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ `put` adds the `item` with given `key` in the cache.
        """
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """ `get` gets an item by key.
        """
        raise NotImplementedError(
            "get must be implemented in your cache class")
