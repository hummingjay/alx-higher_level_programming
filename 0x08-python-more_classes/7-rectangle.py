#!/usr/bin/python3
"""Class that defines a rectangle and its attributes
The height and width.
Then it calculates the area and perimeter.
then addds a string representation of the rectangle
It can check if a rectangle has been deleted and print message
"""


class Rectangle:
    """This defines the rectangle.

    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    number_of_instances = 0

    def __init__(self, print_symbol='#'):
        self.print_symbol = print_symbol

    @property
    def print_symbol(self):
        return self.print_symbol

    @print_symbol.setter
    def print_symbol(self, symbol):
        self.print_symbol = symbol

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        # Increase count when a new instance is created
        Rectangle.number_of_instances += 1

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
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height atribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns a string representation of the rectangle"""
        if self.__width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.__height):
                rectangle_str += f"{Rectangle.print_symbol}" * self.__width
               # rectangle_str += "#" * self.__width
                if i != self.__height - 1:
                    rectangle_str += "\n"
            return rectangle_str

    def __repr__(self):
        """Returns a string representation to recreate the figure"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints message if a rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
