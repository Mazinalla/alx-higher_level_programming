#!/usr/bin/python3

'''function that returns True if the object is exactly an instance of the specified class ; otherwise False'''

def is_same_class(obj, a_class):

    '''compare between the method and attribute of the 2 dir'''

    if dir(obj) == dir(a_class):
        return True
    else:
        return False
