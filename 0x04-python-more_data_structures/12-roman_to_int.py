#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    total = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    p = 0
    for r_index in range(len(roman_string) - 1, -1, -1):
        current = roman_string[r_index]
        current_val = roman.get(current)
        
        if (current_val >= p):
            total += current_val
            p = current_val
        else:
            total -= current_val
            p = current_val
    return total
