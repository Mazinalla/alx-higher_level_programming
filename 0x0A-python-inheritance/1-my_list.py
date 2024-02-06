#!/usr/bin/python3

'''Write a class MyList that inherits from list'''

class MyList(list):

    '''function that prints the list, but sorted (ascending sort)'''

    def print_sorted(self):
        print(sorted(self))
