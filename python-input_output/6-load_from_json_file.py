#!/usr/bin/python3
""" module defines function to load object from json file"""
import json


def load_from_json_file(filename):
    """ this function creates python object from json file"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        return json.load(a_file)
