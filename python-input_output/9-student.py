#!/usr/bin/python3
""" """
class Student(self):
    """ class student initializes student objects """
    def __init__(self, first_name, last_name, age):
        self.firstname = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
