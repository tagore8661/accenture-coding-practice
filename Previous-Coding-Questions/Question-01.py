"""
Character Count -

You are given a string S of length N. Your friend wants to know the number of times his favorite letter C 
occurs in the string. Your task is to help your friend find and return an integer value representing the 
number of times a character occurs in a particular string.

Note: All the characters in the strings are in lowercase,

Input Specification:

input1: A string S
input2: An integer N, representing the length of string
input3: A character C

Output Specification:

Return an integer value representing the number of times a character occurs in a particular string.

Example 1:

input1: helloworld
input2: 10
input3: l

Output: 3
"""

def count_character_occurrences(S, N, C):
    count = 0
    for char in S:
        if char == C:
            count += 1
    return count

# Example usage
S = "helloworld"
N = 10
C = 'l'

print(f"The character '{C}' occurs {count_character_occurrences(S, N, C)} times in the string.")