#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    '''returns a set of all elements in only one set'''
    result = []
    for ele in set_1:
        if ele not in set_2:
            result.append(ele)
    for ele in set_2:
        if ele not in set_1:
            result.append(ele)
    return result
