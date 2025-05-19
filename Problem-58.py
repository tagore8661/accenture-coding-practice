"""
You are given array A, having some dividends further, yougare given 3 numbers D, Q and R.
A dividend can be found using a rule that states:

Dividend Divisor x Quotient + Remainder

Your task is to find and return an integer value representing the index of the dividend if present in array.

If dividend not found return -1
"""

def find_dividend_index(A, D, Q, R):
    # Calculate the dividend using the given formula
    dividend = D * Q + R
    
    # Check if the dividend is present in the array A
    if dividend in A:
        return A.index(dividend)
    else:
        return -1

# Example usage:
A = [10, 20, 30, 40, 50]
D = 5
Q = 6
R = 10
print(find_dividend_index(A, D, Q, R))  # Output will be 3 (since 5*6+10 = 40, which is at index 3)