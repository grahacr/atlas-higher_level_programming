#!/usr/bin/python3
""" this module defines function that adds two integers """
def add_integer(a, b=98):
    """ This function adds two integers and returns result """
    if type(a) != int or type(a) != float:
        raise TypeError("a must be an integer")
    if type(a) != int or type(b) != float:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        return int(a)
    if isinstance(b, float):
        return int(b)
    return (a + b)