#!/usr/bin/python3

'''function that adds a new attribute to an object'''
def add_attribute(obj, attr_name, attr_value):
    """ Adds a new attribute to an object if possible """
    if hasattr(obj, '__dict__') or hasattr(obj, '__slots__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
