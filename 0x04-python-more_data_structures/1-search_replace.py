#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''
    function that replaces all occurrences of an element by another in a new list
    '''
    new_list = my_list
    for i in new_list:
        if i + 1 == search:
            new_list[i] = replace
        else:
            continue
    return new_list