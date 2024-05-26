#!/usr/bin/python3

def best_score(a_dictionary):
    '''Check if the dictionary is empty'''
    if not a_dictionary:
        return None
    max_key = max(a_dictionary)
    return max_key
