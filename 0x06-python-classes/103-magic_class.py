#!/usr/bin/python3
""" creating a magic class"""
import math
""" math module"""
class MagicClass:
    """ define a MagicClass"""
    def __init__ (self, radius):
        """ initializing private  attribute radius
        Args:
            self: self initialization
            radius: object variable
        Raises:
            TypeError: if radius is not an integer or a float"""

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius
    @property
    def area(self):
        """ get area of current square"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ get circumference of current square"""
        return 2 * math.pi* self.__radius
