"""
Even Odd -

Jack has an array A of length N. He wants to label whether the number in the array is even or odd. 
Your task is to help him find and return a string with labels even or odd in sequence according 
to which the numbers appear in the array.

Input Specification:

input1: An integer array A, representing the array of numbers
input2: A integer N, representing the length of array

Output Specification:

Return a string with labels even or odd in sequence according to which the numbers appear in 
the array.

Example 1:

input1 : [1,2,3,4,5,6]
input2 : 6

Output : OddEvenOddEvenOddEven
"""

def even_odd_labels(input1, input2):
    # input1: List of numbers (A)
    # input2: Length of the array (N)
    
    labels = []  # To store the labels (Even or Odd)
    
    # Loop through the array
    for num in input1:
        if num % 2 == 0:
            labels.append('Even')  # Append "Even" for even numbers
        else:
            labels.append('Odd')  # Append "Odd" for odd numbers
    
    # Join the labels into a single string
    return ''.join(labels)
    #return "".join(map(str,labels))


# Example:
input1 = [1, 2, 3, 4, 5, 6]
input2 = 6

print(even_odd_labels(input1, input2))