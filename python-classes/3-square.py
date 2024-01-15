#!/usr/bin/python3
""" This module defines a class named Square with variables and functions
"""


class Square:
    """ This class defines a square with size"""
    def __init__(self, size=0):
        """ This method initiates a square with integer size above 0"""
        if size.isfloat():
            self.__size = size
            elif size < 0:
                raise ValueError("size must be >= 0")
            elif:
                raise TypeError("size must be an integer")
    def area(self):
        """ This method returns the square area of size"""
        if self.size:
            sqArea = size x size
            return sqArea
