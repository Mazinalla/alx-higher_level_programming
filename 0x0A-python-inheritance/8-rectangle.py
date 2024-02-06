#!/usr/bin/python3

'''class Rectangle that inherits from BaseGeometry (7-base_geometry.py)'''

class Rectangle(BaseGeometry):

    '''function that Instantiation with width and height'''

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
