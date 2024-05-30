#!/usr/bin/python3
'''
this module define Rectangle class with two parameter:
1 - width(optional)
1 - height(optional)
'''


class Rectangle:
    '''
    class Rectangle that defines a rectangle by.
    '''
    def __init__(self, width=0, height=0):
        '''
        method for Instantiation with optional parameter:
        - width
        - height
        '''
        self.__width = width
        self.__height = height
    @property
    def width(self):
        '''
        method to get private width from instance(getter)
        '''
        return self.__width
    @property
    def height(self):
        '''
        method to get private height from instance(getter) 
        '''
        return self.__height    
    @width.setter
    def width(self, value):
        '''
        method to set new value to private width(setter)
        '''
        if(+value):
            raise TypeError("width must be an integer")
        elif(value < 0):
            raise ValueError ("width must be >= 0")
        else:
            self.__width = value    
    @height.setter
    def height(self, value):
        '''
        method to set new value to private height(setter)
        '''
        if(+value):
            raise TypeError("width must be an integer")
        elif(value < 0):
            raise ValueError ("width must be >= 0")
        else:
            self.__height = value