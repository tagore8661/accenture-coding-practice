"""
Count of Prime Numbers Divisible by a Given Number -

Write a program that takes three positive integers m, n, and d as input. The program
should count how many prime numbers between m and n (both inclusive) are divisible
by d. Use a while loop to calculate this and print the result.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
m = int(input("Enter start value (m): "))
n = int(input("Enter end value (n): "))
d = int(input("Enter divisor (d): "))
count = 0
num = m
while num <= n:
    if is_prime(num) and num % d == 0:
        count += 1
    num += 1
print("Count of primes divisible by", d, ":", count)
