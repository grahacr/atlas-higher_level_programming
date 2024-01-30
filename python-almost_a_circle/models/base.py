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
        """ method for converting to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ('[]')
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """ class method to save json strings to file"""
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as file:
            dict_json = [obj.to_dictionary() for obj in list_objs]
            string_json = cls.to_json_string(dict_json)
            file.write(string_json)
