#!/usr/bin/python3
""" module for subclass Square via Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ create Square class inherited from Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """initialize instance of square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ replace string conductor to print attributes of square """
        return "[Square] ({}) {}\{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
