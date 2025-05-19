"""The function def differenceofSum(n. m) accepts two integers n, m as arguments 
Find the sum of all numbers in range from 1 to m(both inclusive) that are not divisible by n.
 Return difference between sum of integers not divisible by n with sum of numbers divisible by n."""

def diff_count(m,n):
    sum_div =0
    sum_not_div =0
    for i in range(1,m+1):
        if i % n == 0 :
            sum_div += i

        else :
            sum_not_div += i
    return sum_not_div-sum_div
print(diff_count(int(input()),int(input())))