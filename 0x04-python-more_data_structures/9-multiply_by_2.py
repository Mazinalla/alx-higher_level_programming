#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''a function that returns a new dictionary with all values multiplied by 2'''
    new_dic = {}
    for key in a_dictionary:
        a_dictionary[key] **= 2
        new_dic[key] = a_dictionary[key]
    return new_dic