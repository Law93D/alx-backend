#!/usr/bin/env python3
""" 100-lfu_cache module """

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.cache_data = {}
        self.freq = {}
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the existing item
            self.cache_data[key] = item
            self.update_freq(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the LFU items
            min_freq = min(self.freq.values())
            lfu_keys = [k for k, v in self.freq.items() if v == min_freq]

            # If multiple LFU items, use LRU for eviction
            if len(lfu_keys) > 1:
                # Get the least recently used (LRU) item among the LFU items
                lru_key = next(iter(self.order))
            else:
                lru_key = lfu_keys[0]

            # Discard the LFU item
            del self.cache_data[lru_key]
            del self.freq[lru_key]
            self.order.pop(lru_key)
            print("DISCARD: {}".format(lru_key))

        # Insert the new item
        self.cache_data[key] = item
        self.freq[key] = 1
        self.order[key] = None
        self.update_freq(key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and move to end of order
        self.update_freq(key)
        return self.cache_data[key]

    def update_freq(self, key):
        """ Update the frequency of a key """
        if key not in self.freq:
            return

        freq = self.freq[key]
        self.freq[key] = freq + 1
        self.order.move_to_end(key)
