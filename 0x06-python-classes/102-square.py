#!/usr/bin/python3

'''class define square'''

class Square:
    '''
    A class representing a square.

    Attributes:
    - __size (int): The length of each side of the square.
    '''
    def __init__(self, size=0):
        '''
        Initializes a Square instance with an optional specified side length.

        Parameters:
        - size (int, optional): The length of each side of the square. Default is 0.
        '''
        self.size = size

    @property
    def size(self):
        '''
        property to retrieve size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        property to set the value

        para:
        - value of the size
        '''
        if not isinstance(value, int,float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        '''
        puplic method that returns the current square area
        '''
        return self.__size ** 2
    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __ge__(self, other):
        return self.size >= other.size