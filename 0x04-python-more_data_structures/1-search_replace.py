#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''Create a new list to store the modified elements'''
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
