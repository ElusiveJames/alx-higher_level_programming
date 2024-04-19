#!/usr/bin/python3
""" Add_interger module
    This module add two integers and return their sum.
    It verify  for all possible user inputs
    before finding their sum
 """


def add_integer(a, b=98):
    """ Function to find sum
    of two integers and  else will raise TypeError
    """
    if not type(a) in [float, int]:
        raise TypeError("a must be an integer")
    if not type(b) in [float, int]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
