"""
Given an array of integers, write a function that finds the maximum element and its index.

 Input: [1,8,4,9,6]
 Output: (9,3)
"""

def find_max_and_index(arr):
    max_value = max(arr)
    max_index = arr.index(max_value)
    return (max_value, max_index)

# Sample Test Case
arr = [1, 8, 4, 9, 6]
print(find_max_and_index(arr))  # Output: (9, 3)