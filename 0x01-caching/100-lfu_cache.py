#!/usr/bin/python3

""" 100-lfu_cache """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Defines a LFU caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Adds an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                least_freq_keys = [key for key, freq in self.frequency.items() if freq == min(self.frequency.values())]
                least_recent_key = min(least_freq_keys, key=lambda x: self.cache_data[x])
                del self.cache_data[least_recent_key]
                del self.frequency[least_recent_key]
                print("DISCARD:", least_recent_key)
            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        return self.cache_data[key]
