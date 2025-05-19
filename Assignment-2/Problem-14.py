"""
Generate the Sequence of Harmonic Numbers -

Write a program that takes a positive integer n as input. The program should generate
and print the first n harmonic numbers using a while loop. The n-th harmonic number
is defined as H(n)=1+12+13+...+1nH(n) = 1 + \frac{1}{2} + \frac{1}{3} + ... + \frac{1}{n}
H(n)=1+21+31+...+n1

"""

n = int(input("Enter number of terms: "))
i = 1
harmonic_sum = 0
while i <= n:
    harmonic_sum += 1 / i
    print(f"H({i}) = {harmonic_sum}")
    i += 1
