#!/usr/bin/python3
""" Module defines a class named Square with fields """


class Square:
    """ class defines a square by private instance attribute size"""
    def __init__(self, size=0):
        """ method initializes a simple square if size is digit above 0"""
        if isinstance(size, int):
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
