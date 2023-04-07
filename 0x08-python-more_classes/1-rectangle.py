#!/usr/bin/python3
"""Empty class that defines a rectangle"""


class Rectangle:
    """This defines the rectangle.

    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ defines the attrinute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """takes in the value and returns certain errors
        where necessary
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Defines the height atribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
