#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

Rectangle.print_symbol = "C"
my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)

Rectangle.print_symbol = "H"
my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
