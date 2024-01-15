#!/usr/bin/python3
""" module creates a square based on positioning, with various methods """


class Square:
    """ Class initializes a square """
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
        """ method to set size of square to new value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @position.setter
    def position(self, value):
        """ method to define positioning of square """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ method to return current square area of Square """
        return (self.__size * self.__size)
    
    def my_print(self):
        """method to print square """
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range (0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
