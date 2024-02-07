#!/usr/bin/python3

'''import json module'''
import json

'''function that returns an object (Python data structure) represented by a JSON string'''
def from_json_string(my_str):

    '''returns an object represented by a JSON string'''
    return json.load(my_str)
