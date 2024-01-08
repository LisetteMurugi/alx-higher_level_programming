#!/usr/bin/python3
"""
1-my_list Module
"""


class MyList(list):
    """MyList class that inherits from list"""
    def __init__(self):
        """To initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
