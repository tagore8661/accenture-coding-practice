""" 
Chocolate Distribution -

The function accepts an integer array 'arr' of size 'n' as its argument. Each element of 'arr' represents the number 
of chocolates distributed to a person. The function needs to return the minimum number of chocolates that need to be 
distributed to each person so that the difference between the chocolates of any two people is minimized.

Example:

Input:
n: 5
arr: 10 4 12 3 1	 	

Output: 	 	
3

"""


def min_chocolates(arr):
    arr.sort()

    min_diff = arr[-1] - arr[0]
    for i in range(len(arr) - 4):
        min_diff = min(min_diff, arr[i + 4] - arr[i])

    return min_diff

arr = [10, 4, 12, 3, 1]
result = min_chocolates(arr)
print(result)