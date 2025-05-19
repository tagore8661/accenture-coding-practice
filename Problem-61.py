"""
Problem Statement: John is trying to determine whether a number is prime for a math project. 
A prime number is defined as a number greater than 1 that has no divisors other than 1 and itself. 
He needs to write a program that checks if a given number is prime. If the number is prime, 
the program should output 1; otherwise, it should output 0. Help John by writing a program 
that reads an integer n and prints 1 if it is a prime number, and O if it is not.
"""

def check_prime(n):
    if n <=1 :
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
        
    return True

n = int(input("Enter a number : "))
if check_prime(n):
    print("1")
else:
    print("0")