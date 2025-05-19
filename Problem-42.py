"""
You are given two integers A and B Your task is to find and return an 
integer representing the value of their bitwise OR operation.

Note : 
    1 OR 0 = 1
    0 OR 1 = 1
    1 OR 1 = 1
    0 OR 0 = 0

Example :
    input1 - 5
    input2 - 9

    output - 13
"""

def convert(a,b):
    return a|b

c = int(input())
d = int(input())

print(convert(c,d))