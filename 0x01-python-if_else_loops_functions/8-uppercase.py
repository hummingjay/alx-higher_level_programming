#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # if string lowercase convert to upper using Ascii
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
            print("{}".format(char), end="")
    print()
