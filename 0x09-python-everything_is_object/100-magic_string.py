#!/usr/bin/python3
def magic_string():
    result = "\n".join([", ".join(["BestSchool"] * (i + 1))for i in range(10)])
    return result
