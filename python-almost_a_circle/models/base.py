#!/usr/bin/python3
""" this module includes class Base"""
import json


class Base:
    """ base class manages id of other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize instance of Base class with id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)
