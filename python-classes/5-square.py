#!/usr/bin/python3
""" Class Square defines a square with methods to define and write """


class Square:
    """ Class defines a square """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ method to retrieve size of Square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ method sets size of Square to new value:
        - must be an integer
        - must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ method to return current square area of Square """
        return (self.__size * self.__size)

    def my_print(self):
        """ method to print square """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
