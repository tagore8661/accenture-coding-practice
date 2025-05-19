"""
Product of First N Prime Numbers -

Write a program that takes a positive integer n as input. The program should calculate
the product of the first n prime numbers using a while loop and print the result.

"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter the number of primes: "))
product = 1
count = 0
num = 2
while count < n:
    if is_prime(num):
        product *= num
        count += 1
    num += 1
print("Product of first", n, "prime numbers:", product)
