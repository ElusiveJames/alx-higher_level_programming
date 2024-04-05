#!/usr/bin/python3
""" creating an empty class that define a square"""


class Square:
    """ define a square"""
    def __init__(self, size=0):
        """ initializing private  attribute size
        Args:
            self: self initialization
            size: object variable
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is negative."""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """getter method just return the attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """return area of current square"""
        return (self.__size ** 2)

    def my_print(self):
        """print the square using #"""
        if self.__size == 0:
            print('')
        for i in range(0, self.__size):
            [print('#', end='')for j in range(self.__size)]
            print('')
