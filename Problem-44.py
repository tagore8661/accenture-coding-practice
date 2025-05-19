"""
your are given a string S of length N . your friend wants to know the number of times
his favorite letter C occurs in the string. your task is to help your friend find and
return an integer value representing the number of times a character occurs in a 
particular string.
 
input1:helloworld
input2: 10 
input3: l 

output : 3
"""

def count_occurrences(S, C):
    return S.count(C)

# Example usage:
S = "helloworld"
C = "l"
print(count_occurrences(S, C))  # Output: 3