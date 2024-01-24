#!/usr/bin/python3
""" """


def class_to_json(obj):
    dict_obj = obj.to_dict()
    json_dict = json.dumps(dict_obj)
    return json_dict
