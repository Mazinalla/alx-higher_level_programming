#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    '''a function that deletes a key in a dictionary.'''
    
    if key in a_dictionary:
        a_dictionary.pop(key)
        return a_dictionary
    else:
        return a_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print(new_dict)

new_dict = simple_delete(a_dictionary, 'track')
print(new_dict)