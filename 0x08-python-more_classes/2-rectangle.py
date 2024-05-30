#!/usr/bin/python3
'''
class of Rectangle
'''


class Rectangle:
    '''
    class Rectangle that defines a rectangle with two optional parameter:
    - width
    - height
    '''
    def __init__(self, width=0, height=0):
        '''
        method that construct the instance:
        '''
        self.width = width
        self.height = height
    
    @property
    def width(self):
        '''
        method to retrive height(getter)
        '''
        return self.__width
    
    @property
    def height(self):
        '''
        method to retrive height(getter)
        '''
        return self.__height
    
    @width.setter
    def width(self, value):
        if(not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif(value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
        
    @height.setter
    def height(self, value):
        if(not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif(value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
    
    def area(self):
        area = self.__width * self.__height
        return area
    
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)