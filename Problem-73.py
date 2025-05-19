#finds the largest number that can be formed by permutation

# Write a program that accepts the integer array of length ‘size’ and finds the largest number that can be formed by permutation.

"""Explanation:

compare helps determine that 9 should come before 5, 5 before 34, etc.

custom_sort arranges the array in the order [9, 5, 34, 3, 30].

largest_number joins these values to produce 9534330."""

def compare(a, b):
    return (str(a) + str(b)) > (str(b) + str(a))

def custom_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if not compare(arr[i], arr[j]):
                arr[i], arr[j] = arr[j], arr[i]

def largest_number(arr):
    custom_sort(arr)
    result = ''.join(map(str, arr))
    return result if result[0] != '0' else '0'

# Example usage
arr = [3, 30, 34, 5, 9]
print(f"The largest number formed is {largest_number(arr)}")  # Output should be 9534330