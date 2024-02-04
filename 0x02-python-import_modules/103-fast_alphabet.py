#!/usr/bin/python3
import functools, operator, string
print(functools.reduce(operator.concat, map(lambda x: (x+'\n',), list(string.ascii_uppercase))))
