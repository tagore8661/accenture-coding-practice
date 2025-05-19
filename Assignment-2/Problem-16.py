"""
Generate the Factorial Sequence -

Write a program that takes a positive integer n as input. The program should generate
and print the factorial sequence (1!, 2!, 3!, ..., n!) using a while loop.

"""

n = int(input("Enter number of terms: "))
i = 1
factorial = 1
while i <= n:
    factorial *= i
    print(f"{i}! =", factorial)
    i += 1
