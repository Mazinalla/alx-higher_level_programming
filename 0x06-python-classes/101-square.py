#!/usr/bin/python3

'''
class that defines a square
'''

class Square:
    '''
    class that defines a square
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Initializes a square instance with specified size and position

        parameter:
        - size
        - position
        '''
        self.size = size
        self.position = position


    @property
    def size(self):
        '''
        Getter method for the value attribute.

        return:
        The reference to the attribute
        '''
        return self._size
    
    @size.setter
    def size(self, value):
        '''
        Setter method for the value attribute.
        Parameters:
        - value
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    @property        
    def position(self):
        '''
        getter method for the position attr.

        return:
        - 
        '''
        return self._position

    @position.setter
    def position(self, value):
        '''
        setter method for the position attr.
        
        para:
        - value
        ''' 
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value
    
    def area(self):
        '''
        puplic method that return the current square area
        '''
        return self.size ** 2
    
    def my_print(self):
        '''
        puplic method that prints in stdout the square with the character #.
        '''
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)