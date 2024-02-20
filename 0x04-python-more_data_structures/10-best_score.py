#!/usr/bin/python3

def best_score(a_dictionary):
    '''Check if the dictionary is empty'''
    if not a_dictionary:
        return None

    # Find the key with the maximum value
    max_key = max(a_dictionary)
    
    return max_key

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))