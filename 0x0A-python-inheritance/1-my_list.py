#!/usr/bin/python3
""" Class that inhrits from list """


class MyList(list):
    """defined the class inheriting from list"""
    def print_sorted(self):
        """ Method that prints the list but sorted ascending"""
        print(sorted(self))
