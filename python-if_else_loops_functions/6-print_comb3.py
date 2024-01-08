#!/usr/bin/python3
for dig1 in range(10):
    for dig2 in range(10 + 1, 10):
        if dig1 * 10 + dig2 < 89:
            print("{:02d}".format(i * 10 + j), end=", ")
        else:
            print("{:02d}".format(i * 10 + j))
