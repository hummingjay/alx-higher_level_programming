#!/usr/bin/python3
"""Function that checks if object is istance of, or if the object is an instance
of a class that inherited from specified class and returns true for this.
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
