#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """ This class just defines a function to raise an exception"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            ValueError("{} must be greater than 0".format(value))
