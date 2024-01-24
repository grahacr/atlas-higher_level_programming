#!/usr/bin/python3
""" module contains class Student """


class Student:
    """ class Student initializes student objects """
    def __init__(self, first_name, last_name, age):
        self.firstname = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ function to return dictionary of Student """
        return self.__dict__
