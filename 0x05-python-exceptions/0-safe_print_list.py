#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
def safe_print_list(my_list=[], x=0):
    my_list = [1, 2, 3, 4, 5]
    length = 0
    for a in my_list:
        length += 1
    if x <= 0:
        pass
    elif x > 0 and x <= length:
        for i in range(length):
            try:
                print(my_list[i], end="")
                if i == x - 1:
                    break
            except:
                print("invalid")
        print()
    else:
        for i in range(length):
            print(my_list[i], end="")
        print()    
        x = length
    return x
