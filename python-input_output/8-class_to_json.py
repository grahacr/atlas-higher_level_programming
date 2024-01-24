#!/usr/bin/python3
""" module includes function to convert class object """


def class_to_json(obj):
    """ function returns dict description using json serialization"""
    return obj.__dict_
