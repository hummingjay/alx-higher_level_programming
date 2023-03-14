#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    extend = (0,)
    # needs to check how many 0s to add to the tuple if < 2
    if len(tuple_a) < 2:
        tuple_a += extend * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += extend * (2 - len(tuple_b))
    # use only the first 2 integers of the tuple
    a, b = tuple_a[:2]
    c, d = tuple_b[:2]

    # calculate the sum
    return (a + c, b + d)
