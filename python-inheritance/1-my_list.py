#!/usr/bin/python3
"""
This module has a class MyList that inherits from
list. Has a Public instance method print_sorted that
prints the list in ascending order
"""

class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """Initializes the super object"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
