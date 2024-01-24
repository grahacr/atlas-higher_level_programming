#!/usr/bin/python3
""" module creates subclass Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square subclass of Rectangle """
    def __init__(self, size):
        """ initialize instance of Square """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ utilize area method for square size """
        return self.__size * self.__size

    def __str__(self):
        """ print string representation of square object """
        return "[Square] {}/{}".format(self.__size, self.__size)
