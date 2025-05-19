"""
Hike Trial -

You are on a hiking trail represented by an array A of length N. where the trail initially 
ascends and then descends, forming a single peak. Your task is to find and retum an integer 
value representing the elevation of the summit

Input Specification:

input1: An integer array A
input2: An integer value N denoting the size of A

Output Specification:

Return an integer value representing the elevation of the summit.

Example 1:
input1: [1,2,3,4,3,2,1]
input2: 7

Output: 4

Example 1:
input1 = [5, 6, 7, 8, 9, 6, 3, 1]
input2 = 8

Output: 9
"""

def find_summit(A, N):
    # The summit is the maximum element in the array
    return max(A)

# Example usage:
input1 = [1, 2, 3, 4, 3, 2, 1]  # Array representing the hiking trail
input2 = 7  # Size of the array
output = find_summit(input1, input2)
print(f"The elevation of the summit is: {output}")