"""
Prime Numbers in Reverse Order - 

Write a program that takes two positive integers m and n as input. The program should
print all the prime numbers between m and n (both inclusive) in reverse order using a
while loop.
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
num = n
while num >= m:
    if is_prime(num):
        print(num, end=" ")
    num -= 1
