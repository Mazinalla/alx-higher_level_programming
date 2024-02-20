#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    '''Get the sorted list of keys'''
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate through sorted keys and print key-value pairs
    for key in sorted_keys:
        value = a_dictionary[key]

        # Check if the value is a nested dictionary
        if isinstance(value, dict):
            print(f"{key}: ", end="")
            print_sorted_dictionary(value)
        else:
            print(f"{key}: {value}")


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)