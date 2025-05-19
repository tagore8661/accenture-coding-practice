"""
Array Rotation -

The function accepts an integer array 'arr' of size 'n' and an integer 'd' as its argument. The function needs to rotate 
the array 'arr' by 'd' positions to the right. The rotation should be done in place, without using any additional memory.

Example:

Input:
n: 5
arr: 1 2 3 4 5
d: 3
 	 	
Output:
3 4 5 1 2	 	 
"""

def rotate_array(arr, n, d):
    temp = arr[-d:]
    for i in range(n - 1, d - 1, -1):
        arr[i] = arr[i - d]
    arr[:d] = temp

n = 5
arr = [1, 2, 3, 4, 5]
d = 3

rotate_array(arr, n, d)

print("Output:", *arr)