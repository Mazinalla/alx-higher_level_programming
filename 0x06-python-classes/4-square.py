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
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        - int: The length of each side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
        - value (int): The length of each side of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2