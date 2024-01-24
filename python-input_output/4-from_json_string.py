#!/usr/bin/python3
""" module contains function to convert json string """
import json


def from_json_string(my_str):
    """ function takes input json string and converts to python data structure"""
    str = json.loads(my_str)
    return(str)
