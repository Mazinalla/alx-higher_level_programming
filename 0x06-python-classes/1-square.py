#!/usr/bin/python3

'''class that defines a square'''

class Square:

    '''
    class that defines a square
    attr: size
    methode: none
    '''
    def __init__(self, __size):
        self.size = __size
    
    '''calc the square root of size'''
    def square(self):
        self.size ** 2
