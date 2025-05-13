#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    sum = 0
    for num in roman_string:
        sum = sum + roman_table.get(num)
    return sum
