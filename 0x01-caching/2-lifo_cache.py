#!/usr/bin/env python3

"""a class LIFOCache that inherits from BaseCaching and is a caching system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """a class LIFOCache that inherits from BaseCaching and
    is a caching system with put and get methods"""

    def __init__(self):
        """method for initialization"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """assigns to the dictionary self.cache_data
        the item value for the key key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.keys.append(key)
        if len(self.keys) > BaseCaching.MAX_ITEMS:
            discarded_key = self.keys[-2]
            del self.cache_data[discarded_key]
            self.keys.remove(discarded_key)
            print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
