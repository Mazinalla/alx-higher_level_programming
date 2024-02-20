#!/usr/bin/python3

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
def search_replace(my_list, search, replace):
    '''Create a new list to store the modified elements'''
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
