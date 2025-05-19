"""
MAGICAL NUMBER -

You are given a program to find the count of magical numbers from 1 to N.
A magical number is defined by the following criteria:

•	Convert each number in the range 1 to N (inclusive) to its binary representation.
•	Replace '0' with '1' and '1' with '2' in the binary string.
•	Calculate the sum of the digits in the modified binary string. If the resultant
    number odd then it is considered a magical number.

Your task is to find and return an integer value representing the count of the magical
numbers present within the given range.

For N = 5, Output = 2
For N = 10, Output = 4
For N = 15, Output = 7
"""

def is_magical(num):
    # Convert the number to binary and remove the '0b' prefix
    binary_str = bin(num)[2:]

    # Replace '0' with '1' and '1' with '2'
    modified_str = binary_str.replace('1', '2').replace('0', '1')

    # Calculate the sum of digits in the modified binary string
    digit_sum = sum(int(digit) for digit in modified_str)

    # Check if the sum of digits is odd
    return digit_sum % 2 == 1


def count_magical_numbers(N):
    magical_count = 0

    # Iterate through all numbers from 1 to N
    for i in range(1, N + 1):
        if is_magical(i):
            magical_count += 1

    return magical_count


# Example usage:
N = int(input("Enter the value of N: "))
result = count_magical_numbers(N)
print(f"The count of magical numbers from 1 to {N} is: {result}")