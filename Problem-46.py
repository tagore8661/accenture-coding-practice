"""
2) Find the second smallest element in an array

Sample input:
8 3 4 1 6 2

Output: 2
"""

def find_second_smallest(arr):
    # Initialize the smallest and second smallest to infinity
    smallest = float('inf')
    second_smallest = float('inf')
    
    # Iterate through the array to find the smallest and second smallest elements
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    
    return second_smallest

# Example usage:
arr = [8, 3, 4, 1, 6, 2]
print(find_second_smallest(arr))  # Output will be 2