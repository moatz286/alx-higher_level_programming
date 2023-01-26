#!/usr/bin/python3

""" Square class.

"""

class Square:
    """Square class with private instance attribute size"""

    def __init__(self, size):
        """init function 

        Args:
            size (int): int represent the square size.

        """
        self._size = size
