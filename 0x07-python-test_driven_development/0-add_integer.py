#!/usr/bin/python3
"""
add two integer and return the value
"""


def add_integer(a, b=98):
    '''
    function that add two integer
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    elif isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return a + b
