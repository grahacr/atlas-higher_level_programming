#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return
    new_list = [element if i == idx else value for i]
