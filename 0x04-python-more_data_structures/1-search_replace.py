#!/usr/bin/python3

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
def search_replace(my_list, search, replace):
    '''Create a new list to store the modified elements'''
    new_list = []

    '''Iterate through the elements of the original list'''
    for element in my_list:
        '''Replace the element if it matches the 'search' element'''
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)

    return new_list
