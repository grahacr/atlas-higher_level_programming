#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result_dict = {}
    for key, value in a_dictionary.items():
        result_dict[key] = value * 2
    return result_dict
