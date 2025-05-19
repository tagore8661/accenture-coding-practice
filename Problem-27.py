"""
Jack has an Array A of length N he wants to label wheth number in the array is even or odd.
Your task is to help him find and return a string with labels even or odd in sequence according
to rech numbers appear in the array

Input1: [2,3,4]
Input2 : 3

Output : EvenOddEven
"""
"""concat =""

li=[1,2,3,4,5]

for i in li:
    if i%2==0:
        concat+="Even"
    else:
        concat+="0dd"
print(concat) """

concat =""
arr = list(map(int,input().split()))
n = len(arr)
for i in arr:
    if i % 2 == 0:
        concat +=" EVEN"
    else :
        concat +=" ODD"

print(concat)