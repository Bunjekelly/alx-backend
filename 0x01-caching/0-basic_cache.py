#!/usr/bin/env python3

"""a class BasicCache that inherits from BaseCaching and is a caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache that inherits from BaseCaching
    and is a caching system with two methods put and get"""

    def put(self, key, item):
        """assigns to the dictionary self.cache_data
        the item value for the key key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """"returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
