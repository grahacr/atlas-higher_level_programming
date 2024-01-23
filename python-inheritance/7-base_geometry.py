#!/usr/bin/python3
""" module defines BaseGeometry class """


class BaseGeometry:
    """ class BaseGeometry with integer validation functions"""
    def area(self):
        """ method to raise area exception """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ method to validate value as integer and above 0"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
