#YT_Techie CodeBuddy

"""Problem Statement:

In an array a superior element is one which is greater than all the elements to its right side. 
The rightmost element itself be a superior element.

You are given a function, int Find_Number_Of_Superior_Element(int arr[], int n);

The function accepts an integer array and the size of array, Implement the function 
to find the total number of superior elements present in array.

Assumptions:

N>0 and Array index starts from 0

Input: n= 6

arr= [8,10,6,2,9,7]

Output: 3"""

def find_number_of_superior_elements(arr):
    n = len(arr)
    if n == 0 :
        return 0
    count = 1
    max_right_ele = arr[-1]
    for i in range(n-2 , -1 ,-1):
        if arr[i] > max_right_ele:
            count += 1
            max_right_ele = arr[i]
    return count

arr = list(map(int,input().split()))
print(find_number_of_superior_elements(arr))

#Another Way

"""def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))

    count = 0
    sup = float('-inf')

    for i in range(n-1, -1, -1):
        if arr[i] > sup:
            count += 1
            sup = arr[i]

    print(count)

if __name__ == "__main__":
    main() """