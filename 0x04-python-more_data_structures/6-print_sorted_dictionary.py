#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sor_dic = dict(sorted(a_dictionary.items()))
    print(sor_dic)

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
    # for key in a_dictionary:
    #     print(f"{key} => {a_dictionary[key]}")