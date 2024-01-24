#!/usr/bin/python3
""" module includes function to convert class object """


def class_to_json(obj):
    """ function returns dict description using json serialization"""
    dict_obj = obj.to_dict()
    json_dict = json.dumps(dict_obj)
    return json_dict
