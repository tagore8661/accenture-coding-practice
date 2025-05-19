"""
Maximize Pair Product -

Noah is given an integer array A of length N. He must perform the following operations on the array:

    Select any integer pair/s from the array with their sum equal to 18.
    From this select the pair with the maximum product such that the first element of the pair is 
    greater than the second element of the pair.

Your task is to help Noah find and return a pair in the form of an integer array which satisfies the 
conditions mentioned.

Input Specification:

input1: An integer value N. representing the size of array A. 
input2: An integer array A.

Output Specification:
Return a pair in the form of an integer array which satisfies the conditions mentioned.

Example 1:

input1 : 8
input2: {11,1,2,8,10,11,15,7}

Output: {10,8}
"""


def maximize_pair_product(N, A):
    max_product = -1  # Initialize with a negative value to track the max product
    result_pair = []  # To store the resulting pair
    
    # Iterate through all possible pairs in the array
    for i in range(N):
        for j in range(N):
            # Ensure it's not the same element and check sum condition
            if i != j and A[i] + A[j] == 18 and A[i] > A[j]:
                product = A[i] * A[j]  # Calculate product
                
                # Update if the current product is greater than max_product
                if product > max_product:
                    max_product = product
                    result_pair = [A[i], A[j]]
    
    return result_pair

# Example:
input1 = 8
input2 = [11, 1, 2, 8, 10, 11, 15, 7]

print(f"Best pair: {maximize_pair_product(input1, input2)}")