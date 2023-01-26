#!/usr/bin/python3

"""Square model."""


class Square:
    """Initialize Class Square
    Methods
    -------
    area()
        return size of square
    my_print()
        print the square with # in stdout
    """

    def __init__(self, size=0):
        """
        Parameters
        -----------
        size(int):
            size of square.
        """
        self.size = size

    @property
    def size(self):
        """get the value of square size"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return size of square"""
        return (self.size * self.size)

    def my_print(self):
        """print square with #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
