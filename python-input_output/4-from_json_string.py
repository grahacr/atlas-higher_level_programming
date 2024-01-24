#!/usr/bin/python3
""" module contains function to convert json string """
import json


def from_json_string(my_str):
    """ function converts input json string to python object """
    str = json.loads(my_str)
    return (str)
