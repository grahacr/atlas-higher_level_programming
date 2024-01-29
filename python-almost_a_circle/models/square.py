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
        return "[Square] ({}) {}/{} - {}".format(
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

    def update(self, *args, **kwargs):
        """ public method to update values of instance attributes"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'size':
                self.width = value
                self.height = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value
