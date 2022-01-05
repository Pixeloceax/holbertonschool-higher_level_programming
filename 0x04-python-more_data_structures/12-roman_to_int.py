#!/usr/bin/python3
def roman_to_int(roman_string):
    s = []
    i = 0
    num = 0
    while i < len(s):
        if i+1<len(s) and s[i:i+2] in roman_string:
            num+=roman_string[s[i:i+2]]
            i+=2
        else:
            #print(i)
            num+=roman_string[s[i]]
            i+=1
    return num
