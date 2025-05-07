#!/usr/bin/python3
def uppercase(str):
    for c in str:
        o = ord(c)
        if o >= 97 and o <= 122:
            o -= 32
        print('{}'.format(chr(o)), end='')
    print()
