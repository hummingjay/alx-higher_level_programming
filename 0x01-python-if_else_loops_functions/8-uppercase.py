#!/usr/bin/python3
def uppercase(str):
    for up in range(97, 123):
        if chr(up) in str:
            x = chr(up-32)
            print("{}".format(x))
