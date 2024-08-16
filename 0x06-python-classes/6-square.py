#!/usr/bin/python3
""" creating an empty class that define a square"""


class Square:
    """ define a square"""
    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

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

    @property
    def position(self):
        """getter method just return the attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method"""
        if not isinstance(value, tuple) or len(value) != 2 or not\
                all(isinstance(i, int) for i in value) or\
                not all(i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        if any(x <= 0 for x in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """return area of current square"""
        return (self.__size ** 2)

    def my_print(self):
        """print the square using #"""
        if self.__size == 0:
            print('')
        for i in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
