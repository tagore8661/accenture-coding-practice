"""
Generate Arithmetic Sequence -

Write a program that takes three integers a, d, and n as input, where a is the first term,
d is the common difference, and n is the number of terms. The program should
generate and print the arithmetic sequence using a while loop.

a: 3 d: 2 n: 5
3, 5, 7, 9, 11

"""

a = int(input("Enter first term: "))
d = int(input("Enter common difference: "))
n = int(input("Enter number of terms: "))
term = a
count = 1
while count <= n:
    print(term, end=" ")
    term += d
    count += 1
