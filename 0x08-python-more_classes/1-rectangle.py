#!/usr/bin/python3
"""Empty class that defines a rectangle"""


class Rectangle:
    """This defines the rectangle.

    Args:
    width: width side of the rectangle
    height: height side of the rectangle
    """
    def __init__(self, width = 0, height = 0):
        self._width = width
        self._height = height

    @property
    def width(self):
        """ defines the attrinute width"""
        return self._width

    @width.setter
    def width(self, value):
        """takes in the value and returns certain errors
        where necessary
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.width = value

    @property
    def height(self):
        """Defines the height atribute"""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.height = value
