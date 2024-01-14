#!/usr/bin/python3
def print_last_digit(number):
    if number > 10:
        print("{}".format(number % 10))
    else:
        print("{:1d}".format(number))
