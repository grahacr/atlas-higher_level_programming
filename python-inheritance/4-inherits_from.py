#!/usr/bin/python3
""" module defines function checking if object is inherited or instance """
def inherits_from(obj, a_class):
    """ define function that checks if object is instance of class
    - can be either directly or indirectly inherited from specific class """
    return isinstance (obj, a_class) or issubclass(obj.__class__, a_class)
