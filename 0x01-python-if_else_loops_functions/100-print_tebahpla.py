#!/usr/bin/python3
for i in range(97, 123):
    continue
while(i >= 97):
    if i % 2 == 0:
        print("{}".format(chr(i)), end="")
        i -= 1
    else:
        print("{}".format(chr(i - 32)), end="")
        i -= 1
