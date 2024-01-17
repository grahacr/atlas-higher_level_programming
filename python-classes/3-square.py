#!/usr/bin/python3
""" Module 3-square defines class Square with variables and functions """


class Square:
    """ This class defines a square with size"""
    def __init__(self, size=0):
        """ This method initiates a square with integer size above 0"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ This method returns the square area of size"""
        return self.__size * self.__size
