#Kth Largest Element in an Array

def kth_largest(arr, k):
    for i in range(k):
        max_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr[k-1]

# Test
print(kth_largest([3, 2, 1, 5, 6, 4], 2))  # Output: 5 




def exp(arr, k):
    arr.sort()  # Sort the array in place
    print(arr[-k])

exp([3, 2, 1, 5, 6, 4], 2)