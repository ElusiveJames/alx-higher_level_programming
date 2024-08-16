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

    def __eq__(self, other):
        """ override the == operator"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """ override the != operator"""
        return not self == other

    def __gt__(self, other):
        """ override the > operator"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """ override the >= operator"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """ override the < operator"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """ override the <= operator"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
