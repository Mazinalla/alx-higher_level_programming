#!/usr/bin/python3

'''function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class;otherwise False'''

def is_kind_of_class(obj, a_class):
    
    '''return: True if the object is an instance of the specified class or its subclass, otherwise False'''

    return isinstance(obj, a_class)
