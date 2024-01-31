#!/usr/bin/env python3

"""a class FIFOCache that inherits from BaseCaching and is a caching system"""

from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """a class FIFOCache that inherits from BaseCaching
    and is a caching system with get and put methods"""

    def __init__(self):
        """this is a method for initialization"""
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        """ assigns to the dictionary self.cache_data
        the item value for the key key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.keys.append(key)
        if len(self.keys) > BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.popleft()
            del self.cache_data[discarded_key]
            print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
