#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    ''' a function that replaces or adds key/value in a dictionary'''
    lista = list(a_dictionary)
    for i in lista:
        if i == key:
            continue
        else:
            lista.append(key)
    dicta = dict(lista)
    dicta[key] = value
    return dicta