#!/usr/bin/python3
""" module creates a class named Rectangle with methods """


class Rectangle:
    """ class initializes and creates rectangle with private fields """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        max_area_rectangle = max([rect_1, rect_2], key=lambda Rectangle: Rectangle.area())
        return max_area_rectangle

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
        """ method returns area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ method returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ private method to create copy of rectangle for printing """
        copy_str = ""
        if self.__width > 0 and self.__height > 0:
            for row in range(self.__height):
                for column in range(self.__width):
                    copy_str += str(self.print_symbol)
                if row < self.__height - 1:
                    copy_str += '\n'
            return copy_str
        return copy_str

    def __repr__(self):
        """ method to reproduce conductor call for rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
