#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num_el = 0
        for i in my_list:
            print(i, end="")
            num_el += 1
            if (my_list.index(i) + 1) == x:
                break
        print()
        return num_el
