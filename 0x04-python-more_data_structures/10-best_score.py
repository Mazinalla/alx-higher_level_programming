#!/usr/bin/python3

def best_score(a_dictionary):
    '''Check if the dictionary is empty'''
    if not a_dictionary:
        return None
    max_key = None
    max_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
