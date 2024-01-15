#!/usr/bin/python3

"""
This module defines a class named Square with fields
"""


class Square:
    """This class defines a square by private instance attribute size"""
    def __init__(self, size=0):
        """This method initializes a simple square if size is digit above 0"""
        if size.isfloat():
            self.__size = size
            elif:
                raise TypeError("size must be an integer")
                if size < 0:
                    raise ValueError("size must be >= 0")
