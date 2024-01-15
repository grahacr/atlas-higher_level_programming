#!/usr/bin/python3
""" Module defines a class square with several methods and variables """
class Square:
    """ Class defines a square with private instance size and multiple methods"""
    def __init__(self, size=0):
        self.__size = size
    
    @property
    def size(self):
        """ method to retrieve size of class Square"""
        return self.__size
    
    @property
    def size(self, value):
        """ method to set size of class Square to new value if meeting certain critiera:
        - must be an integer
        - must be greater than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        """ method to return the value of the square area of class Square"""
        return self.__size * self.__size
