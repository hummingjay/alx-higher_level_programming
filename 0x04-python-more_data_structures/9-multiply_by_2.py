#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return {}
    new_dict = {}
    for key, value in a_dictionary.items():
        value = value*2
        new_dict[key] = value

    return new_dict
