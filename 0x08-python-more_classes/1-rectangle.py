#!/usr/bin/python3
""" creating a blueprin for rectangle"""


class Rectangle:
    """creating an empty class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """show width"""
        return self.__width

    @width.setter
    def width(self, value):
        """" set value for width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """show the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
