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

        if key in self.cache_data:
            # If the key is already in the cache, remove it from the order
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:

            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the new item to the cache and update the order
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update the order since this key was recently accessed
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
