#The maximum element and its index

arr = list(map(int,input().split()))

max = 0 
index = 0
for i in range(len(arr)):
    if arr[i] > max :
        max = arr[i]
        index =i

print(max)
print(index)