"""
6) Even odd Array

Input : 1,2,6,3,5,3

Output : 1,3,5,3,2,6
"""

def rearrange_even_odd(arr):
    # Separate the odd and even numbers
    odd_numbers = [num for num in arr if num % 2 != 0]
    even_numbers = [num for num in arr if num % 2 == 0]
    
    # Concatenate the odd and even numbers
    rearranged_array = odd_numbers + even_numbers
    return rearranged_array

# Example usage:
arr = [1, 2, 6, 3, 5, 3]
print(rearrange_even_odd(arr))  # Output will be [1, 3, 5, 3, 2, 6]