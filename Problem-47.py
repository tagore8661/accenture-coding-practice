"""
3) Covert the decimal into binary and add it's bits

Smmple input: 10

Output: 2

Explanation: 10 -> 1010 -> 1+0+1+0 -> 2
"""

def sum_of_binary_digits(N):
    # Convert the decimal number to binary and remove the '0b' prefix
    binary_representation = bin(N)[2:]
    # Calculate the sum of the digits in the binary representation
    digit_sum = sum(int(digit) for digit in binary_representation)
    return digit_sum

# Example usage:
N = 10
print(sum_of_binary_digits(N))  # Output will be 2