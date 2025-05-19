"""
Your friend has problem in reading the time if a clock follows 24-hours format,
So you decide to help him out. You have two intgers X and Y. Your tash is to find
and return an integer value representing the product of these two integers in the
12-hours system

Example :
    input1 - 4
    input2 - 5

    output - 8
"""

def convert(a,b):
    return a*b%12  # (a*b)%12 

c = int(input())
d = int(input())

print(convert(c,d))