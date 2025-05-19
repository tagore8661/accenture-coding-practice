#product of smallest pair in given array and that sum is less than the given sum

def  productSmallestPair(sum,arr):
    if not arr or len(arr) < 2 :
        return -1
    arr.sort()
    if arr[0] + arr[1] <= sum:
        return arr[0] * arr [1]
    else:
        return 0
    
sum = int(input())
arr = list(map(int,input().split()))

print(productSmallestPair(sum,arr))