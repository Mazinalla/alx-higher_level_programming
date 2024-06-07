#!/usr/bin/python3
'''
module that print square with the string #
'''


def print_square(size):
    '''
    function that print square with the inputed size

    args:
        size => opthional

    return:
        print square
    '''
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in i:
            print("#", end="")
        print()
