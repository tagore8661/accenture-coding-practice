"""
1. Quotient of Two Numbers -

○ Write a program to take two integers a and b as input and calculate the quotient of a divided by b.
○ Expression: quotient = a / b (consider both integer division and floating-point division)

2. Division Result of Three Numbers -

○ Write a program to take three integers a, b, and c as input and calculate the result of dividing a by b and then by c.
○ Expression: result = a / b / c (consider both integer division and floating-point division)
"""

#1. Quotient of Two Numbers
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
quotient = a / b
print("Quotient (float):", quotient)
print("Quotient (integer):", a // b)


#2. Division Result of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
division_result = a / b / c
print("Result of division (float):", division_result)
print("Result of division (integer):", a // b // c)
