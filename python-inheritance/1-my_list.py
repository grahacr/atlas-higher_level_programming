#!/usr/bin/python3
""" this module creates a class called MyList """
class MyList(list):
    """ subclass MyList inherits from class list """
    def print_sorted(self):
        """ method to print the sorted list """
        list_sort = sorted(self)
        print(list_sort)
