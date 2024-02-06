#!/usr/bin/python3

'''Write a class BaseGeometry (based on 6-base_geometry.py)'''

class BaseGeometry:

    '''function that raises an Exception with the message area() is not implemented'''

    def area(self):
        raise Exception("area() is not implemented")

    '''function that validates value'''

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        else:
            raise ValueError("<name> must be greater than 0")
