#!/usr/bin/python3

""" My List Model"""


class MyList(list):
    """
    This class inherits from the built-in list class and adds a print_sorted method that sorts the list
    in ascending order and prints it.
    """
    def print_sorted(self):
        """
        Sorts the list in ascending order and prints it.
        """
        sorted_list = sorted(self)
        print(sorted_list)
