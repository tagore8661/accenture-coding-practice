"""
Generate Geometric Sequence -

Write a program that takes three integers a, r, and n as input, where a is the first term,
r is the common ratio, and n is the number of terms. The program should generate and
print the geometric sequence using a while loop.

a: 2 r: 3 n: 5
2, 6, 18, 54, 162

"""

a = int(input("Enter first term: "))
r = int(input("Enter common ratio: "))
n = int(input("Enter number of terms: "))
term = a
count = 1
while count <= n:
    print(term, end=" ")
    term *= r
    count += 1
