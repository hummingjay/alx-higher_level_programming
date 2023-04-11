#!/usr/bin/python3
"""Checking if object is an instance of a class that is inherited from class"""


def inherits_from(obj, a_class):
    """Function to take in object and check if is instance of class that
    inherited from specific class
    Args:
        obj - input to check if is an instance of inherited class
        a_class - class that obj should be an instance of
    Return:
        true
        false
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
