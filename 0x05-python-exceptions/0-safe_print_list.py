#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    try:
        num_el = 0
        for i in range(len(my_list)):
            print(my_list[i], end="")
            num_el += 1
            if i + 1 == x:
                break
        print()
        return num_el
    except:
        print("Unknown Errot")
