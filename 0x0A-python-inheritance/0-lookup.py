#!/usr/bin/python3
def lookup(obj):
    attributes_and_methods = dir(obj)
    result = [attr for attr in attributes_and_methods if not attr.startswith('__')]
    return result
