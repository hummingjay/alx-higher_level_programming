#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key.strip() in a_dictionary:
        del a_dictionary[key.strip()]
    return a_dictionary
