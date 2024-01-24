#!/usr/bin/python3
import json
""" module contains function to convert json string to object data struct """


def from_json_string(my_str):
    """ function takes input json string and converts to python data structure"""
    str = json.loads(my_str)
    return(str)
