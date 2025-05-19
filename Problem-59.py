"""
number is a perfect number if is equal to sum of its proper divisors, at is, 
sum of its positive divisors excluding the number itself. Write Function to check if a given number is perfect or not.

input: n = 22
output: 14
divisors of 22 are 1, 2 and 11. Sum of divisors is 14 which is not equal to 22.

input: n = 6
output: 1 
divisors of 6 are 1, 2 and 3. Sum of divisors is 6.
"""

def is_perfect_number(n):
    # Initialize the sum of divisors
    sum_of_divisors = 0
    
    # Iterate over all possible divisors from 1 to n-1
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    
    # Check if the sum of divisors is equal to the number itself
    return sum_of_divisors == n

# Example usage:
n1 = 22
print(is_perfect_number(n1))  # Output will be False (since 1 + 2 + 11 = 14, which is not equal to 22)

n2 = 6
print(is_perfect_number(n2))  # Output will be True (since 1 + 2 + 3 = 6)