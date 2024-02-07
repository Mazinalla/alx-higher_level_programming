#!/usr/bin/python3

'''function that returns the JSON representation'''

def to_json_string(my_obj):
    """ Returns the JSON representation of an object (string) """
    if isinstance(my_obj, (int, float, bool, str, type(None))):
        # Handle simple types
        if isinstance(my_obj, str):
            return f'"{my_obj}"'
        else:
            return str(my_obj)
    elif isinstance(my_obj, list):
        # Handle lists
        return '[' + ', '.join(to_json_string(item) for item in my_obj) + ']'
    elif isinstance(my_obj, dict):
        # Handle dictionaries
        return '{' + ', '.join(f'"{key}": {to_json_string(value)}' for key, value in my_obj.items()) + '}'
    else:
        # Handle unsupported types
        raise TypeError(f"Object of type {type(my_obj)} is not JSON serializable")
