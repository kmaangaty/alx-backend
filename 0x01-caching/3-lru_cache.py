#!/usr/bin/python3

""" 3-lru_cache """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Defines a LRU caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Adds an item to the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.keys.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
