#!/usr/bin/python3
import calculator_1

if __name__ == "__name__":
    a = 10
    b = 5
    
    # define results
    addition = add(a, b)
    subtraction = sub(a, b)
    multiplication = mul(a, b)
    division = div(a, b)

    print("{} + {} = {}".format(a, b, addition))
    print("{} + {} = {}".format(a, b, subtraction))
    print("{} + {} = {}".format(a, b, multiplication))
    print("{} + {} = {}".format(a, b, division))
