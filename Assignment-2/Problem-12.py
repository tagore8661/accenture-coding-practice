"""
Prime Factorization of a Number -

Write a program that takes a positive integer n as input. The program should print the
prime factorization of n using a while loop.

"""

n = int(input("Enter a number: "))
factor = 2
while n > 1:
    if n % factor == 0:
        print(factor, end=" ")
        n //= factor
    else:
        factor += 1
