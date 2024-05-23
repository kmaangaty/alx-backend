#!/usr/bin/python3

""" 4-mru_cache """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Defines a MRU caching system """

    def put(self, key, item):
        """ Adds an item to the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.pop(key)
        self.cache_data[key] = key
        return self.cache_data[key]
