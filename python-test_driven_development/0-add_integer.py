#!/usr/bin/python3
""" this module defines function that adds two integers """
def add_integer(a, b=98):
    """ This function adds two integers and returns result """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return int(a + b)