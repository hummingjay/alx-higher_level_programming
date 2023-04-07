#!/usr/bin/python3
"""Class that defines a rectangle
calculates the width and height and returns them.
Then returns the string representation of the rectangle
"""


class Rectangle:
    """Class that defines a rectangle and its attributes.

    Args:
        width (int) - width of the rectangle
        height (int) - height of the rectangle
    """ 
    def __init__(self, width=0, height=0):
        """instantiation with optional height and width"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for width attribute"""
        self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute"""
        self.__height

    @height.setter
    def height(self):
        """Setter for the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError(value, int):
                raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width * self.__height))
    def __str__(self):
        """Returns a string representation of the rectangle"""
        if self.__width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.__height):
                rectangle_str += "#" * self.__width + "\n"
            return rectangle_str

    def __repr__(self):
        """Returns a string representation that can be used to recreate the figure"""
        return f"Recatngle(width={self.__width}, height={self.__height})"
