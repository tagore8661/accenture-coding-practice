"""
Even Odd -

Jack has an array A of length. N. He wants to label whether the number in the array is even or odd. Your task is to 
help him find and return a string with labels even or odd in sequence according to which the numbers appear in the array.

Input Specification:

input1: An integer array A, representing the array of numbers
input2: A integer N, representing the length of array

Output Specification:

Return a string with labels even or odd in sequence according to which the numbers appear in the array.

Example 1:

input1: [1,2,3,4,5,6]
Input2:6

Output: OddEvenOddEvenOddEven
"""

def even_odd_labels(A, N):
    labels = []
    for num in A:
        if num % 2 == 0:
            labels.append("Even")
        else:
            labels.append("Odd")
    return ''.join(labels)

# Example usage
A = [1, 2, 3, 4, 5, 6]
N = 6

print(f"The sequence is: {even_odd_labels(A, N)}")