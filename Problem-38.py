""" The function def differentofSum(n,m) accept two integer n,m as arguments,
find the sum of all numbers in rage from 1 to m (both inclusive) that are not divisible by n .
Return different between sum of integers not divisible by n with sum of numbers divisible by n"""

"""def differentofSum(n,m):
    sum_not_divisible = sum(i for i in range(1,m+1) if i %
                            n==0)
    sum_divisible = sum(i for i in range(1,m+1) if i % n
                        != 0)
    return abs(sum_divisible -sum_not_divisible)

n = int(input())
m = int(input())
print(differentofSum(n,m))"""


def differenceOfSum(n,m):
    sum_div = 0
    sum_not_div = 0
    for i in range(1,m+1):
        if i % n == 0:
            sum_div += i
        else :
            sum_not_div += i

    return abs(sum_div - sum_not_div)

n = int(input())
m = int(input())

print(differenceOfSum(n,m))