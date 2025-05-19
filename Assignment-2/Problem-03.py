"""
Difference Between the Largest and Smallest Prime Numbers in a Range -

Write a program that takes two positive integers m and n as input. The program should
calculate the difference between the largest and the smallest prime numbers between
m and n (both inclusive) using a while loop and print the result. If no prime numbers
exist in the range, print "No prime numbers found."

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
smallest = None
largest = None
num = m
while num <= n:
    if is_prime(num):
        if smallest is None or num < smallest:
            smallest = num
        if largest is None or num > largest:
            largest = num
    num += 1
if smallest is not None and largest is not None:
    print("Difference:", largest - smallest)
else:
    print("No prime numbers found")
