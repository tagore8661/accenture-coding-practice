"""
Check if Sum of Prime Numbers is Even or Odd -

Write a program that takes two positive integers m and n as input. The program should
calculate the sum of all prime numbers between m and n (both inclusive) using a while
loop. Then, check if the sum is even or odd, and print the result.

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
total = 0
num = m
while num <= n:
    if is_prime(num):
        total += num
    num += 1
if total % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")
