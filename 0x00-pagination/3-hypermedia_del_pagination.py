#!/usr/bin/env python3

from typing import Dict

class Server:
    # ... (existing code)

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''
            get_hyper_index: function
            description: returns a page content depending on the index
                         and the page size
            @self: Object constructor.
            @index: Start index of the page.
            @page_size: the size of page.
            return: A dictionary containing information about the specific page.
        '''
        assert index is None or (isinstance(index, int) and index >= 0), "Invalid index"
        assert isinstance(page_size, int) and page_size > 0, "Invalid page size"

        dataset = self.indexed_dataset()
        total_items = len(dataset)
        if index is None:
            index = 0
        else:
            assert index < total_items, "Index out of range"

        next_index = min(index + page_size, total_items)
        data = [dataset[i] for i in range(index, next_index)]

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data,
        }

# Example usage in 3-main.py
# ... (existing code)

# 1- request first index
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next index
print(server.get_hyper_index(res.get('next_index'), page_size))

# 3- remove the first index
del server._Server__indexed_dataset[res.get('index')]
print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 4- request again the initial index
print(server.get_hyper_index(index, page_size))

# 5- request again initial next index
print(server.get_hyper_index(res.get('next_index'), page_size))

