#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and is a caching system using LFU algorithm.
    """
    def __init__(self):
        """ Initialize the LFU cache.
        """
        super().__init__()
        self.freq_count = {}  # To keep track of the frequency count of each key

    def put(self, key, item):
        """ Add an item to the cache using LFU algorithm.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequency used item
                lfu_key = min(self.freq_count, key=lambda k: self.freq_count[k])
                if len([k for k, v in self.freq_count.items() if v == self.freq_count[lfu_key]]) > 1:
                    # If more than 1 item with the least frequency, use LRU algorithm to discard the least recently used
                    lru_key = min(self.order, key=lambda k: self.order.index(k))
                    del self.cache_data[lru_key]
                    del self.freq_count[lru_key]
                    self.order.remove(lru_key)
                    print("DISCARD: {}".format(lru_key))
                else:
                    del self.cache_data[lfu_key]
                    self.order.remove(lfu_key)
                    print("DISCARD: {}".format(lfu_key))
                    del self.freq_count[lfu_key]
            self.cache_data[key] = item
            self.order.append(key)
            self.freq_count[key] = self.freq_count.get(key, 0) + 1

    def get(self, key):
        """ Get an item from the cache by key.
        """
        if key is not None and key in self.cache_data:
            # Update the frequency count of the key
            self.freq_count[key] += 1
            return self.cache_data[key]
        return None

# Driver code
if __name__ == "__main__":
    my_cache = LFUCache()

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
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()
