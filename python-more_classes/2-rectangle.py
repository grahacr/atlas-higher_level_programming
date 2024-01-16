#!/usr/bin/python3
""" module creates a class named Rectangle with methods """


class Rectangle:
    """ class initializes and creates rectangle with private fields """
    def __init__(self, width=0, height=0):
        """ method initializes instances of Rectangle """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def height(self):
        """ method to retrieve height of rectangle """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ method to set height of rectangle if int and above 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ method to retrieve width of rectangle """
        return self.__width
    
    @width.setter
    def width(self, value):
        """ method to set width of rectangle if int and above 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
