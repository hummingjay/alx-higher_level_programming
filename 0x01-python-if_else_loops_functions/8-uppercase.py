#!/usr/bin/python3
def uppercase(str):
    for up in range(65, 91):
        if str == chr(up+32):
            return chr(up)
