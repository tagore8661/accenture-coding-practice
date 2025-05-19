#ProductSmallPair
def ProductSmallPair(arr,n,sum):
    if n < 2 :
        return -1
    arr_sort = sorted(arr)
    for i in range(n-1):
        if arr_sort[i]+arr_sort[i+ 1] <= sum:
            return arr_sort[i]*arr_sort[i+1]
        else :
            return 0
        
arr =list(map(int,input().split()))
n = len(arr)
sum =int(input())

print(ProductSmallPair(arr,n,sum))


"""n = int(input())
sum1 = int(input())
arr = list(map(int, input().split()))
if n < 2:
    print('-1')
arr = sorted(arr)
for i in range(n-1):
    if arr[i] + arr[i+1] < sum1:
        print(arr[i] * arr[i+1])
        break
else:
    print('0')"""