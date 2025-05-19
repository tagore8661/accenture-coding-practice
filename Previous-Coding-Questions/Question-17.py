"""
Prime Number Picnic -

You are planning a picnic for a group of friends who love math. To make interesting, 
you decided to bring unique numbers of items, N. Your task is to find and return an 
integer value representing the sum of all the prime numbers till N in case, the number
of items is 0 or 1, return 0.

Note: Prime numbers are natural numbers that are divisible by only 1 and the number 
itself

Input Specification:

Input1: An integer value N

Output Specification:

Return an integer value representing the sum of all the prime num case, the number 
of items is 0 or 1, return 0.

Example 1:

input1: 10
Output: 17

Explanation :

Step 1: Check all numbers from 2 to 10 to see if they are prime:
2: Prime (sum = 2).
3: Prime (sum = 2 + 3 = 5).
4: Not prime.
5: Prime (sum = 5 + 5 = 10).
6: Not prime.
7: Prime (sum = 10 + 7 = 17).
8, 9, 10: Not prime.
Total sum: 17

Output: 17

"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(N):
    # Special case for N <= 1
    if N <= 1:
        return 0
    
    # Sum all prime numbers less than or equal to N
    prime_sum = 0
    for num in range(2, N + 1):
        if is_prime(num):
            prime_sum += num
    
    return prime_sum


# Example usage:
input1 = 10  # Example input
output = sum_of_primes(input1)
print(f"Sum of prime numbers till {input1}: {output}")