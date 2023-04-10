#!/usr/bin/pyhton3
def magic_string(n):
    return ', '.join(['BestSchool' + (', BestSchool' * i) \
        for  i in range(n)]) # list comprehension
