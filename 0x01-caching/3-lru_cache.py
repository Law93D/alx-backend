#!/usr/bin/env python3
"""
LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data):
                if self.order:
                    lru_key = self.order[-1]
                    del self.cache_data[lru_key]
                    self.order.pop()
                    print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None

    def print_cache(self):
        """ Print the cache content """
        print("Current cache:")
        for key in self.cache_data:
            print("{}: {}".format(key, self.cache_data[key]))
