#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx < 1:
            return None
        elif idx > len(my_list):
            return None
        else:
            return my_list[idx]
