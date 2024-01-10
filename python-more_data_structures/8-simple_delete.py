#!/usr/bin/python
def simple_delete(a_dictionary, key=""):
    delete_this = key
    del a_dictionary[delete_this]
    return a_dictionary
