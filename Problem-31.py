"""What is a prime number?

A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
In other words, a prime number is a whole number greater than 1. whose only two whole-number factors are 1 and itself. 
The first few prime numbers are 2, 3, 5, 7. 11. 13. 17. 19, 23, and 29.

Given an array with 'N' elements, you are expected to find the sum of the values that are present in prime indexes of the array. 
Note that the array index starts with 0 i.e. the position (index) ofthe first array element is 0, the position of the next array element is 1. and so on.

Example 1: If the array elements are [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]. then the values at the prime index are 30.40.60.80 and their sum is 210. 
Example 2, If the array elements are (-1, -2,-3, 3, 4,-7), then the values at the prime index are -3, 3. -7 and their sum is -7. 
Example 3; If the array elements are (-4, 5), there are no prime index values. So, the sum should be returned as 0."""

def is_prime(num):
    if num <= 1:
        return False
    if num ==2:
        return True
    for i in range(2,num//2 + 1):
        if num % i == 0:
            return False
    return True

def sum_of_prime_index_number(arr):
    sum = 0 
    for j in range(len(arr)):
        if is_prime(j):
            sum += arr[j]
    return sum

arr = list(map(int,input().split()))
print(sum_of_prime_index_number(arr))