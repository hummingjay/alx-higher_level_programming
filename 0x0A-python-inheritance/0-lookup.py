#!/usr/bin/python3
"""Deefines an attribute object lookup function"""


def lookup(obj):
    """Function that returns the list of available attributes and methods"""
    attr_and_methods = dir(obj)
    return attr_and_methods
