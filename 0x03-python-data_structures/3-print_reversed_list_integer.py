#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1):
        i += 1
    while i >= 0 :
        print(f"{my_list[i]}")
        i -= 1
