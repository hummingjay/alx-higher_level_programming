#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__name__":
    a = 10
    b = 5
    
    # define results
    addition = add(a, b)
    subtraction = sub(a, b)
    multiplication = mul(a, b)
    division = div(a, b)

    print("{} + {} = {addition}".format(a, b))
    print("{} + {} = {subtraction}".format(a, b,))
    print("{} + {} = {multiplication}".format(a, b))
    print("{} + {} = {division}".format(a, b))
