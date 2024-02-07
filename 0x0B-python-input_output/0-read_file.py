#!/usr/bin/python3

'''function that reads a text file'''
def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout """
    with open(filename, mode='r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
