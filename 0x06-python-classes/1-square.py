#!/usr/bin/python3

""" Square class.

"""


class Square:
    """
    A class that defines a square.

    Attributes:
    __size (int): The size of the square.

    Methods:
    area(): Returns the area of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class with the given size.

        Args:
        size (int): The size of the square.
        """

        self.__size = size
