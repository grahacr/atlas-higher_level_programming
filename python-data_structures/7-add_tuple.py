#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    return (tuple(elem1 + elem2 for elem1, elem2 in zip(tuple_a, tuple_b)))
