#!/usr/bin/python3
for i in range(10):
    # making (i, j) are always unique pairs in order
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print('{}{}'.format(i, j))
        else:
            print('{}{}'.format(i, j), end=', ')
