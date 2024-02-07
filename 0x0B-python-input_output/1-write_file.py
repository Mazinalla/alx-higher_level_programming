#!/usr/bin/python3

''' function that writes a string to a text file'''
def write_file(filename="", text=""):

    '''function that write on text file'''
    with open(filename, mode="w", encoding="UTF8") as file
    content = file.write(text)

    '''return length of the text'''
    return len(text)
