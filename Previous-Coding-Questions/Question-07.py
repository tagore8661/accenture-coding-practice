"""
Maximum Permutation Value -

You are given a string array of length N. Your task is to find and retum an integer value representing 
the maximum permutation count of the strings after removing all the vowels from every elements in the 
string array.

Note:
   Consider all the letters in the string as different 
   If there are no permutable characters then return 0
   The string consists of both uppercase and lowercase characters

Input Specification:

input1: A string array of length N
input2: An integer N. representing the size of the string array

Output Specification:

Retum an integer value representing the maximum permutation count of the string elements.

Example 1 :

input1 :{hello,ccbc,aaeiou}
input2 :3

Output : 24
"""


import math

def max_permutation_value(input1, input2):
    # input1: List of strings (array of length N)
    # input2: Size of the array N
    
    vowels = set("aeiouAEIOU")  # Set of vowels (both lowercase and uppercase)
    max_permutations = 0  # Variable to store the maximum permutation value
    
    # Loop through each string in the array
    for s in input1:
        # Remove vowels from the string
        filtered_string = ''.join([char for char in s if char not in vowels])
        
        # Calculate the length of the remaining characters
        length = len(filtered_string)
        if length > 0:
            # If there are characters left, calculate the factorial (permutations)
            permutations = math.factorial(length)
            max_permutations = max(max_permutations, permutations)
    
    return max_permutations if max_permutations > 0 else 0

# Example:
input1 = ["hello", "ccbc", "aaeiou"]
input2 = 3

print(max_permutation_value(input1, input2))


import math

def remove_vowels(s):
    return ''.join(char for char in s if char.lower() not in 'aeiou')

def max_permutation_count(strings, n):
    max_permutations = 0
    
    for string in strings:
        no_vowels = remove_vowels(string)
        if no_vowels:
            permutations = math.factorial(len(no_vowels))
            if permutations > max_permutations:
                max_permutations = permutations
    
    return max_permutations if max_permutations > 0 else 0

# Example usage
strings = ["hello", "ccbc", "aaeiou"]
n = 3

print(f"Maximum permutation count: {max_permutation_count(strings, n)}")