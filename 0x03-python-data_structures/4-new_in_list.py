#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list is None:
        my_list = []
    else:
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            new = mylist.copy()
            new[idx] = element
            return new
