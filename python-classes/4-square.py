#!/usr/bin/python3
""" Module defines a class square with several methods and variables """


class Square:
    """ Class defines square with private instance size and methods"""
    def __init__(self, size=0):
        """ initialize a simple square """
        self.__size = size

    @property
    def size(self):
        """ method to retrieve size of class Square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ method sets size of class Square to new value:
        - must be an integer
        - must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ method to return the value of the square area of class Square"""
        return (self.__size * self.__size)
