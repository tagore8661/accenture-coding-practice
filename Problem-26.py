"""You are given an A of length N.Your task is to find and return an integer value
representing the difference between the SUM of elements at odd index and XOR of elements at even index."""

def sum_diff(arr):
    even_arr = 0
    odd_arr = 0
    for i in range(len(arr)):
        if i % 2 == 0 :
            even_arr ^= arr[i]
        else:
            odd_arr += arr[i]
    return  odd_arr - even_arr

arr = list(map(int,input().split()))
print(sum_diff(arr))