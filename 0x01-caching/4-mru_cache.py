#!/usr/bin/env python3
"""Task 4: MRU Caching.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A class MRUCache that inherits from BaseCaching and implements
    a caching system based on the Most Recently Used (MRU) algorithm.
    """

    def __init__(self):
        """Initializes the MRU cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache."""
        if key is None or item is None:
            return

        # Check if key already exists
        if key in self.cache_data:
            # Update item and move it to front
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            # Add new item
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # Remove the most recently used item
                mru_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", mru_key)
            # Add the new item and mark it as most recently used
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Retrieves an item from the cache by key."""
        if key is not None and key in self.cache_data:
            # Move the item to front (most recently used)
            self.cache_data.move_to_end(key, last=False)
        # Return the item if found, otherwise None
        return self.cache_data.get(key, None)
