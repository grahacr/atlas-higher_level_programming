#!/usr/bin/python3
""" """"
class Rectangle:
    """ """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return(self.__width)

    @property
    def height(self):
        return(self.__height)

    @property.width_setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
    @property.height_setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
