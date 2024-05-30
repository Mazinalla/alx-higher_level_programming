#!/usr/bin/python3
'''
This module defines the Rectangle class with specific attributes and methods.
'''


class Rectangle:
    '''
    Class Rectangle that defines a rectangle.
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
        Method for instantiation with optional parameters:
        - width
        - height
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''
        Method to get the private width from the instance (getter)
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Method to set a new value to the private width (setter)
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        Method to get the private height from the instance (getter)
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Method to set a new value to the private height (setter)
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
        Method to calculate the area of the rectangle
        '''
        return self.width * self.height

    def perimeter(self):
        '''
        Method to calculate the perimeter of the rectangle
        '''
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        '''
        Method to provide a string representation of the rectangle
        '''
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for _ in range(self.height):
            rect_str += str(self.print_symbol) * self.width + "\n"
        return rect_str.strip()  # Remove the trailing newline character

    def __repr__(self):
        '''
        Method to provide a string representation of the rectangle
        that can be used to recreate the instance
        '''
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''
        Method to print a message when an instance of Rectangle is deleted
        '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
