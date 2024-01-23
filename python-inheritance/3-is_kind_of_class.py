#!/usr/bin/python3
""" module defines a function to check if object is instance"""


def is_kind_of_class(obj, a_class):
    """ function checks if object is of class or parent class """
    return isinstance(obj, a_class)
