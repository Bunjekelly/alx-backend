#!/usr/biin/env python3

"""a class LRUCache that inherits from BaseCaching and is a caching system"""

from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """a class LRUCache that inherits from BaseCaching and is
    a caching system with put and get methods"""

    def __init__(self):
        """method for initialization"""
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        """assigns to the dictionary self.cache_data
        the item value for the key key"""
        if key is None or item is None:
            return
        if key in self.keys:
            self.keys.remove(key)
        elif len(self.keys) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.popleft()
            del self.cache_data[discarded_key]
            print('DISCARD: {}'.format(discarded_key))
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
