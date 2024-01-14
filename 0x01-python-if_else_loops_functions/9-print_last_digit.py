#!/usr/bin/python3
def print_last_digit(number):
    if number > 10:
        print("{:1d}".format(number % 10))
    else:
        print("{}".format(number))
