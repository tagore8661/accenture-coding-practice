"""
Find the GCD of Two Numbers -

Write a program that takes two positive integers a and b as input. The program should
calculate the greatest common divisor (GCD) of a and b using a while loop and print the
result.

"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b:
    a, b = b, a % b
print("GCD:", a)
