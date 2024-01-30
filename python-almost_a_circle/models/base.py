#!/usr/bin/python3
""" this module includes class Base"""
import json
import sys
from os.path import isfile


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

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method to save json strings to file"""
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as file:
            dict_json = [obj.to_dictionary() for obj in list_objs]
            string_json = cls.to_json_string(dict_json)
            file.write(string_json)

    @staticmethod
    def from_json_string(json_string):
        """ create objects from json string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method to create new instances """
        if cls.__name__ == "Rectangle":
            new_inst = cls(1, 1)
        if cls.__name__ == "Square":
            new_inst = cls(1)
        new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """method to load json string, convert to list of objects and return instance list"""
        filename = "{}.json".format(cls.__name__)
        if not isfile(filename):
            return []
        with open(filename, 'r') as file:
            objects_list = cls.from_json_string(file.read())
        instance_list = []
        for obj in objects_list:
            instance_list.append(cls.create(**obj))
        return instance_list
