"""
Reverse Array - 

lan has been given an array A of length N and he wants to find the sum of even positions after reversing the array. 
Your task is to help him find and return an integer value representing sum of the array elements present at the 
even positions of the reversed array.

Input Specification:

Input: A reversed integer array A
input2: An integer N. representing length of the array

Output Specification:

Return an integer value representing sum of the array elements present at the even positions of the array.

Example 1:

input1: {10,20,30,40,50,60}
input2: 6

Output: 120

Explanation

Here the array A is ={10,20,30,40,50,60} and reversed array is {60,50,40,30,20,10} and length is 6. 
The elements at the even position are 60, 40 and 20. The sum of the alettents is 60+40+20 =120. 
Therefore, 120 is returned as the output.
"""

def sum_even_positions_after_reverse(arr, n):
    # Reverse the array
    reversed_arr = arr[::-1]
    
    # Sum elements at even positions (0-based index)
    even_position_sum = sum(reversed_arr[i] for i in range(0, n, 2))
    
    return even_position_sum

# Example usage
arr = [10, 20, 30, 40, 50, 60]
n = 6

print(f"Sum of elements at even positions after reversing the array: {sum_even_positions_after_reverse(arr, n)}")




def sum_even_positions(input1, input2):
    # input1: The array A (to be reversed)
    # input2: Length of the array N
    
    reversed_array = input1[::-1]  # Reverse the array
    total_sum = 0  # Initialize the sum
    
    # Loop through the reversed array and sum elements at even positions (1-based index)
    for i in range(0, input2, 2):  # Starting from index 1, step by 2 (even positions in 1-based index)
        total_sum += reversed_array[i]  # Add the element at even position
    
    return total_sum

# Example:
input1 = [10, 20, 30, 40, 50, 60]
input2 = 6

print(sum_even_positions(input1, input2))