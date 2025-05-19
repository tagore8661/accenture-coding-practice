"""
Array Equilibrium -

The function accepts an integer array 'arr' of size 'n' as its argument. The function needs to return the index of an 
equilibrium point in the array, where the sum of elements on the left of the index is equal to the sum of elements on 
the right of the index. If no equilibrium point exists, the function should return -1.

Example:

Input:
n: 5
arr: 1 3 5 7 3

Output:
3
"""

def find_equilibrium(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        total_sum -= arr[i]
        if left_sum == total_sum:
            return i
        left_sum += arr[i]

    return -1

arr = [1, 3, 5, 1, 3]
print(find_equilibrium(arr))