"""
Generate Triangular Numbers -

Write a program that takes a positive integer n as input. The program should generate
and print the first n triangular numbers (1, 3, 6, 10, ...) using a while loop.

"""

n = int(input("Enter number of terms: "))
i = 1
while i <= n:
    triangular = i * (i + 1) // 2
    print(triangular, end=" ")
    i += 1
