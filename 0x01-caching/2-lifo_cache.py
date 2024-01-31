#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and is a caching system using LIFO algorithm.
    """
    def __init__(self):
        """ Initialize the LIFO cache.
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache using LIFO algorithm.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last item (LIFO)
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key.
        """
        if key is not None:
            return self.cache_data.get(key)

# Driver code
if __name__ == "__main__":
    my_cache = LIFOCache()

    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()

    my_cache.put("E", "Battery")
    my_cache.print_cache()

    my_cache.put("C", "Street")
    my_cache.print_cache()

    my_cache.put("F", "Mission")
    my_cache.print_cache()

    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
