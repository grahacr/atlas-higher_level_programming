#!/usr/bin/python3
""" module contains save_to_json_file function """
import json


def save_to_json_file(my_obj, filename):
    """ function writes object to text file using json"""
    json_vers = json.dumps(my_obj)
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(json_vers)
