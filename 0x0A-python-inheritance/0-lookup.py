#!/usr/bin/python3
def lookup(obj):
    # Use dir() to get the list of attributes and methods
    attributes_and_methods = dir(obj)

    # Filter out private and special methods (those starting with '__')
    result = [attr for attr in attributes_and_methods if not attr.startswith('__')]

    return result
