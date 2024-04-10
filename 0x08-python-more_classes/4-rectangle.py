#!/usr/bin/python3
""" creating a blueprin for rectangle"""


class Rectangle:
    """creating an empty class"""
    def __init__(self, width=0, height=0):
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

    def area(self):
        """ calculate area"""
        return self.__height * self.__width

    def perimeter(self):
        """find the perimeter"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
            return perimeter
        else:
            perimeter = ((self.__width + self.__height) * 2)
            return perimeter

    def __str__(self):
        """print string representation in human readable format"""
        if self.__width == 0 or self.__height == 0:
            return str()
        string = (('#' * self.__width) + '\n') * self.__height
        return string[:-1]

    def __repr__(self):
        """ return string repesentation of the object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return f"Rectangle({self.width}, {self.height})"
