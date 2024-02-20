#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = {}
    for key in a_dictionary:
        a_dictionary[key] **= 2
        new_dic[key] = a_dictionary[key]
    return new_dic

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)

print(new_dict)