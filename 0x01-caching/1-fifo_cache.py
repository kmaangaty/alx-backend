#!/usr/bin/python3

""" 1-fifo_cache """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Defines a FIFO caching system """

    def put(self, key, item):
        """ Adds an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
