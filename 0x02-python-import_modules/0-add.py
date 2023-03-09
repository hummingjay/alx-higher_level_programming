#!/usr/bin/python3
# import the function from add_0.py
from add_0 import add

# check if module is run as main by using __name__
if __name__ == "__main__":
    a = 1
    b = 2
    # call the function add
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
