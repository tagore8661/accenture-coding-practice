"""
Write a code calculates the sum of the squares of the first n natural numbers.

"""

n = int(input())

#summ = sum(i** 2 for i in range(1, n + 1))
summ = 0
for i in range(1,n+1):
    summ = summ +i ** 2

print(summ)