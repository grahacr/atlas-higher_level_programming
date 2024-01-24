#!/usr/bin/python3
""" This module creates class Rectangle from inherited BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ create subclass Rectangle"""
    def __init__(self, width, height):
        """initialize instance of Rectangle using base method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
