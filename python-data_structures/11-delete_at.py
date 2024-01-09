#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = [elem for elem in my_list if elem != idx]
        return new_list
