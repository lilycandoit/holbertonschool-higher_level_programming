#!/usr/bin/python3

"""
This module defines the MyList class that inherits from list
and adds a method to print the sorted list.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    Adds a method to print the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        sorted() returns a sorted copy of the list;
        it doesn't change the original.
        """
        print(sorted(self))
