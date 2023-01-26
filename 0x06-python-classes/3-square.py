!/usr/bin/python3

"""Square model."""


class Square:
    """
    Class Square with praivte int size.
    Methods
    -------
    area()
        return current square area
    """
    def __init__(self, size=0):
        """__init__ size of square
        Parameters
        ---------
        size(int):
            size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Return area of Square object
        """
        return (self.__size * self.__size)
