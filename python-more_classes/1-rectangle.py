#!/usr/bin/python3
""" module creates a class named Rectangle """
class Rectangle:
    """ class creates rectangle with height and width attributes """
    def __init__(self, width=0, height=0):
        """ method defines private instance attributes width and height """
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """ method to retrieve width of rectangle """
        return(self.__width)

    @property
    def height(self):
        """ method to retreive height of rectangle """
        return(self.__height)

    @width.setter
    def width(self, value):
        """ method to set width of rectangle if int and above 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ method to set height of rectangle if int and above 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
