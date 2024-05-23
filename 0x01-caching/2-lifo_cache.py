#!/usr/bin/python3

""" 2-lifo_cache """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Defines a LIFO caching system """

    def put(self, key, item):
        """ Adds an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
