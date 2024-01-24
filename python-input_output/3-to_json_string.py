#!/usr/bin/python3
""" module contains function for converting input to json """
import json


def to_json_string(my_obj):
    """function takes input object - string - and converts to json """
    json_vers = json.dumps(my_obj)
    return json_vers
