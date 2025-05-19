"""
Fibonacci Sequence Up to a Given Number -

Write a program that takes a positive integer n as input. The program should print the
Fibonacci sequence up to n using a while loop. The Fibonacci sequence starts with 0
and 1, and each subsequent number is the sum of the previous two.

"""

n = int(input("Enter the limit: "))
a, b = 0, 1
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
