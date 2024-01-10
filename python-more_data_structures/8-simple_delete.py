#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    delete_this = key
    del a_dictionary[delete_this]
    return a_dictionary
