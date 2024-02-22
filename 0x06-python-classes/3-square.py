#!/usr/bin/python3
'''class of square in'''


class Square:
    """
    A class representing a square.

    Attributes:
    - __size (int): The length of each side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional specified side length.

        Parameters:
        - size (int, optional): The length of each side of the square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        '''
        Public instance method that returns the current square area
        '''
        return self.__size ** 2