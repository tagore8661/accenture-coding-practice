"""
Generate Multiplication Table -

Write a program that takes a positive integer n as input. The program should generate
and print the multiplication table for n using a while loop up to 10.

"""

n = int(input("Enter the number for the table: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1
