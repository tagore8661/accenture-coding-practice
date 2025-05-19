"""
You are given a decimal number N. Your task is to convert it to binary and return the sum of its digits.
"""

def sum_of_binary_digits(N):
    # Convert the decimal number to binary and remove the '0b' prefix
    binary_representation = bin(N)[2:]
    # Calculate the sum of the digits in the binary representation
    digit_sum = sum(int(digit) for digit in binary_representation)
    return digit_sum

# Example usage:
N = 10
print(sum_of_binary_digits(N))  # Output will be 2 (binary representation of 10 is '1010')