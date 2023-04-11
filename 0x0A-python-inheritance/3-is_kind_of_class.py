#!/usr/bin/python3
"""Function that checks if object is istance of, or if the object is an instance
of a class that inherited from specified class and returns true for this.
"""


def is_kind_of_class(obj, a_class):
    """ Function that takes in the object and class to check if is instance
    Args:
        obj - object to be checked if is in class or inherited
        False - class or inherited class
    Returns:
        true if is instance of class or inherited class
        false if otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
