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

    def area(self):
        """return area of current square"""
        return (self.__size ** 2)

    def my_print(self):
        """print the square using #"""
        if self.__size == 0:
            print('')
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(' ', end='')for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print('')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """setter method for position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
