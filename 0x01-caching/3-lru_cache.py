#!/usr/bin/env python3
""" 3-lru_cache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # If the cache is full, remove the least recently used item
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the new item to the cache and update the order
        self.cache_data[key] = item

        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update the order to reflect that the key was recently used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]

    def print_cache(self):
        """ Print the current cache """
        print("Current cache:")
        for key in self.cache_data:
            print(f"{key}: {self.cache_data[key]}")
