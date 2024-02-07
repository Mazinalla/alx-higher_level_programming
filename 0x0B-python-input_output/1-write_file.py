#!/usr/bin/python3

''' function that writes a string to a text file'''
def write_file(filename="", text=""):

    '''function that write on text file'''
    with open(filename, mode="w", encoding="UTF8") as file
    num_characters_written = file.write(text)

    '''function that return length of the text'''
    return num_characters_written
