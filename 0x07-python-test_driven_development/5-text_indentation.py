#!/usr/bin/python3
"""
module that print text with 2 lines after each of these char (. - ? - :)

args:
    text(str) => text that must be passed as an argument
"""


def text_indentation(text):
    '''
    function that print the text with 2 lines after each of the following char(. - ? - :)

    args:
        text => the text that entered by the user
    
    return:
        print the text
    '''
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        if i == "." or i == "?" or i == ":":
            print("",end="\n\n")
        print(i, end="")