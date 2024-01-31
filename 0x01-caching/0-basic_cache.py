#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and is a caching system.
    """
    def put(self, key, item):
        """ Add an item to the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key.
        """
        if key is not None:
            return self.cache_data.get(key)

# Driver code
if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.print_cache()

    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()

    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))

    my_cache.print_cache()

    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()

    print(my_cache.get("A"))
