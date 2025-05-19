#LargeSmallSum

def LargeSmallSum(arr,n):
    odd_arr =[]
    even_arr =[]
    for i in range(n):
        if i %2 == 0:
            even_arr.append(arr[i])
        else:
            odd_arr.append(arr[i])

    even_sort=sorted(even_arr)
    odd_sort=sorted(odd_arr)

    return even_sort[len(even_arr)-2] + odd_sort[1]
arr = list(map(int,input().split()))
n = len(arr)

print(LargeSmallSum(arr,n))


"""length = int(input())
arr = list(map(int, input().split()))
even_arr = []
odd_arr = []
for i in range(length):
    if i % 2 == 0:
        even_arr.append(arr[i])
    else:
        odd_arr.append(arr[i])
even_arr = sorted(even_arr)
odd_arr = sorted(odd_arr)
print(even_arr[len(even_arr)-2] + odd_arr[len(odd_arr)-2])"""