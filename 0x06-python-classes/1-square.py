#!/usr/bin/python3
'''class that defines a square'''


class Square:
    """
    A class representing a square.

    Attributes:
    - __size (int): The length of each side of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a specified side length.

        Parameters:
        - size (int): The length of each side of the square.
        """
        self.__size = size
