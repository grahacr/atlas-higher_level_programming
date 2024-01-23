#!/usr/bin/python3
""" module defines function is_same_class """


def is_same_class(obj, a_class):
    """ function checks if object is instance of specified class """
    return obj.__class__ == a_class
