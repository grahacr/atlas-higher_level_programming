#!/usr/bin/python3
""" Module for subclass Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ create Rectangle class inherited from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize rectangle class with private attributes """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return area of rectangle class """
        return self.__height * self.__width

    def display(self):
        """ public method to display rectangle """
        display_str = ""
        if self.height == 0 or self.width == 0:
            return display_str
        for y in range(self.height):
            for x in range(self.width):
                display_str += str('#')
            if y != self.height - 1:
                display_str += '\n'
        return display_str
