#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and is a caching system using MRU algorithm.
    """
    def __init__(self):
        """ Initialize the MRU cache.
        """
        super().__init__()
        self.order = []  # To keep track of the order of item usage

    def put(self, key, item):
        """ Add an item to the cache using MRU algorithm.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item (MRU)
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item from the cache by key.
        """
        if key is not None:
            # Update the order of item usage
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)

# Driver code
if __name__ == "__main__":
    my_cache = MRUCache()

    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()

