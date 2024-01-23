#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
def safe_print_list(my_list=[], x=0):
    my_list = [1, 2, 3, 4, 5]
    if x <= 0:
        pass
    elif x > 0 and x <= len(my_list):
        for i in range(len(my_list)):
            try:
                print(my_list[i], end="")
            except:
                if i == x - 1:
                    break
        print()
    else:
        for i in range(len(my_list)):
            print(my_list[i], end="")
        print()    
        x = len(my_list)
    return x
