"""
Product Pair -

You are given an integer array A of length N and your task is to find and return an integer 
value representing the count of unique pairs whose products are multiples of 3

Note: A Unique pair means that the elements must be the same regardless of their order. 
For instance, (1,3) and (3,1) are considered as the same pair

Input Specification:

input1: An integet value N, representing the size of the array
input2: An integer array A

Output Specification:

Return an integer value representing the count of unique pairs whose products are multiples of 3.

Example 1:

input1:4
input2: (3,6,5,4)

Output: 5

Explanation :

Step 1: We will check all pairs (i, j):
Pair (3, 6): Product = 3 * 6 = 18, which is divisible by 3. Count += 1.
Pair (3, 5): Product = 3 * 5 = 15, which is divisible by 3. Count += 1.
Pair (3, 4): Product = 3 * 4 = 12, which is divisible by 3. Count += 1.
Pair (6, 5): Product = 6 * 5 = 30, which is divisible by 3. Count += 1.
Pair (6, 4): Product = 6 * 4 = 24, which is divisible by 3. Count += 1.
Pair (5, 4): Product = 5 * 4 = 20, which is not divisible by 3. No increment.
Total count: 5 pairs.

Output: 5
"""

def count_pairs_multiple_of_3(N, A):
    # Initialize a counter for the number of valid pairs
    count = 0
    
    # Iterate through all unique pairs (i, j) where i < j
    for i in range(N):
        for j in range(i + 1, N):
            # Check if the product of A[i] and A[j] is divisible by 3
            if (A[i] * A[j]) % 3 == 0:
                count += 1
                
    return count


# Example usage:
N = 4
A = [3, 6, 5, 4]  # Input array

result = count_pairs_multiple_of_3(N, A)
print(f"Total unique pairs whose product is a multiple of 3: {result}")