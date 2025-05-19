#Second Largest Occurences

def findsLargest(nums):
    largest, secondLargest = float('-inf'), float('-inf')
    for num in nums:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num < largest:
            secondLargest = num
    return secondLargest

def findOccSlargest(k, nums):
    count = 0
    for num in nums:
        if num == k:
            count += 1
    return count

n = int(input())
nums = list(map(int, input().split()))

#1 step find second largest
secondLargest = findsLargest(nums)
#2 step find occurences
count = findOccSlargest(secondLargest, nums)
print(count)