#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] != "c" and my_string[i] != "C":
            print(my_string[i], end="")
        else:
            pass
    print("")
    return my_string
