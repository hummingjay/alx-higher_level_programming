#!/usr/bin/python3
""" Function should return True if instance of specific class else False"""


def is_same_class(obj, a_class):
    """ Function takes in object checks if instance of class
    Args:
        obj - any input object to be  checked
        a_class - class/type to be refrenced to
    Return:
        true - if object == specified class
        false - if otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
