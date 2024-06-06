#!/usr/bin/python3
"""
add two integer and return the value
"""


def add_integer(a, b=98):
    '''
    Adds two integers or floats, converting floats to integers before adding.

    Args:
    a: The first number (int or float).
    b: The second number (int or float), defaults to 98.

    Returns:
    The sum of a and b as an integer.

    Raises:
    TypeError: If either a or b are not integers or floats.

    Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    elif isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return a + b
