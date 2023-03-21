#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    # max returns key with largest value
    return (max(a_dictionary, key=a_dictionary.get))
