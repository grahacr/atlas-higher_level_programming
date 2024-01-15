#!/usr/bin/python3
"""
"""
class Square:
    """ Class defines a square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    
    @property
    def size(self):
        """ method to retrieve size of square """
        return (self.__size)
    
    @property
    def position(self):
        """ method to retrieve position """
        return (self.__position)

    @size.setter
    def size(self, value):
        """
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @position.setter
    def position(self, value):
        """ """
            if not isinstance(value, tuple) or len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
    
    def area(self):
        """ method to return current square area of Square """
        return (self.__size * self.__size)
    