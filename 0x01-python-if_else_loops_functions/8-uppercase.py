#!/usr/bin/python3
def uppercase(str):
    current_c = ''
    for c in range(len(str)):
        current_c = str[c]
        if current_c >= 'a' and current_c <= 'z':
            current_c = chr(ord(current_c) - 32)

        if c == len(str) - 1:
            print(current_c)
            break

        print(current_c, end='')
