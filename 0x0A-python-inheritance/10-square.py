#!/usr/bin/python3

'''Defines a class Square that inherits from Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle

'''class Square that inherits from Rectangle'''
class Square(Rectangle):

    '''Instantiation function'''
    def __init__(self, size):

        '''args'''
        super().integer_validator("size", size)
        self.__size = size

        '''function that give the area of square'''
        def area(self):
        """Return the area of the rectangle."""
        return self.__size ** 2
