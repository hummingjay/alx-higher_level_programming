#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    # traverse list
    for i in my_list:
        # make new list
        new_list = []
        # now fill list with append replacing where needed
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
