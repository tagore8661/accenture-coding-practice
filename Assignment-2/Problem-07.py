"""
Sum of Alternating Prime Numbers in a Range -

Write a program that takes two positive integers m and n as input. The program should
calculate the sum of every second prime number between m and n (both inclusive)
using a while loop and print the result.

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
index = 1
total = 0
num = m
while num <= n:
    if is_prime(num):
        if index % 2 == 0:
            total += num
        index += 1
    num += 1
print("Sum of every second prime:", total)
