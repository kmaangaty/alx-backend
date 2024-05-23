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
                most_recent_key = max(self.cache_data, key=self.cache_data.get)
                del self.cache_data[most_recent_key]
                print("DISCARD:", most_recent_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
