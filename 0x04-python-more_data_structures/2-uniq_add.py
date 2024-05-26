#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''function that adds all unique integers in a list'''
    new_list = set(my_list)
    result = sum(new_list)
    return result
