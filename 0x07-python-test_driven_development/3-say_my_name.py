#!/usr/bin/python3
'''
this module is for saying the first and second name
'''


def say_my_name(first_name, last_name=""):
    '''
    function that say for user: my name is bla bla
    
    args:
        first name => mandatory
        last name => opthional
    
    return:
        My name is <first name> <last name>
    '''
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")