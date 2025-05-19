"""
Sum XOR -

You are given an array A of length N. Your task is to find and retum an integer value representing the difference 
between the sum of elements at odd index and XOR of elements at even index.

Input Specification:

input1: An integer N, representing the length of array 
input2: An integer array A

Output Specification:

Retum an integer value representing the difference between the sum of elements at odd index and XOR of elements 
at even index.

Example 1:

input1: 6
input2: (10,5,6,3,7,2)

Output:-1

Explanation:

Here N is 6 and the array A = (10,5,6,3,7,2). The sum of elements at odd positions are 5+3+2=10 and the XOR of 
elements at even positions are 10 XOR 6 XOR 7 =11 and the difference is 10-11=-1. Therefore, -1 is returned as the output.
"""

def sum_xor_difference(n, arr):
    odd_sum = 0
    even_xor = 0

    for i in range(n):
        if i % 2 == 0:  # even index
            even_xor ^= arr[i]
        else:  # odd index
            odd_sum += arr[i]

    return odd_sum - even_xor

# Example usage
n = 6
arr = [10, 5, 6, 3, 7, 2]

print(f"The difference is: {sum_xor_difference(n, arr)}")