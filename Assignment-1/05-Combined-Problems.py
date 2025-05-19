"""
1. Mixed Operations with Two Numbers -

○ Write a program to take two integers a and b as input and calculate the sum, difference, product, and quotient.
○ Expressions:
▪ sum = a + b
▪ difference = a - b
▪ product = a * b
▪ quotient = a / b (consider both integer division and floating-point division)

2. Mixed Operations with Three Numbers -

○ Write a program to take three integers a, b, and c as input and calculate the sum, difference, product, and
result of dividing the sum of a and b by c.
○ Expressions:
▪ sum = a + b + c
▪ difference = a - b - c
▪ product = a * b * c
▪ result = (a + b) / c (consider both integer division and floating-point division)

"""

#1. Mixed Operations with Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient (float):", a / b)
print("Quotient (integer):", a // b)

#2. Mixed Operations with Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Sum:", a + b + c)
print("Difference:", a - b - c)
print("Product:", a * b * c)
print("Result of (a + b) / c (float):", (a + b) / c)
print("Result of (a + b) // c (integer):", (a + b) // c)
