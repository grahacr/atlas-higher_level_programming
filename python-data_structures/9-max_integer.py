#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return
    else:
        largest_int = my_list[0]
        for num in my_list[1:]:
            if num > largest_int:
                largest_int = num
        return largest_int
