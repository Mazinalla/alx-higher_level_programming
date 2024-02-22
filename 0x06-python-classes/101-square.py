#!/usr/bin/python3

'''
Define a class Square.
'''

class Square:
    """
    Square class represents a square with a size and position.

    Attributes:
    - size (int): The size of the square.
    - position (tuple): The position of the square as a tuple of two positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square (default is 0).
        - position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        - int: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
        - value (int): The size to set.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
        - tuple: The position of the square.
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Parameters:
        - value (tuple): The position to set.

        Raises:
        - TypeError: If position is not a tuple of two positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            any(i <= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' in stdout.

        If size is equal to 0, prints an empty line.
        Uses the position to adjust the output by using space.

        Printing a Square instance should have the same behavior as my_print().
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)