#!/usr/bin/env python3

"""a class BasicCache that inherits from BaseCaching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache"""

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]