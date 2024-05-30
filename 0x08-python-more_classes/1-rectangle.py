#!/usr/bin/python3
'''
This module defines the Rectangle class with two parameters:
1 - width (optional)
2 - height (optional)
'''

class Rectangle:
    '''
    Class Rectangle that defines a rectangle.
    '''
    def __init__(self, width=0, height=0):
        '''
        Method for instantiation with optional parameters:
        - width
        - height
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''
        Method to get the private width from the instance (getter)
        '''
        return self.__width

    @property
    def height(self):
        '''
        Method to get the private height from the instance (getter)
        '''
        return self.__height

    @width.setter
    def width(self, value):
        '''
        Method to set a new value to the private width (setter)
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''
        Method to set a new value to the private height (setter)
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
