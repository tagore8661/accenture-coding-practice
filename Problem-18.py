"""The function accepts 2 positive integer ‘m’ and ‘n’ as its arguments.
You are required to calculate the sum of numbers divisible both by 3 and 5, between ‘m’ and ‘n’ both inclusive and return the same."""

def Calculation(num1,num2):
    result = []
    for i in range(num1,num2):
        if (i % 3 ==0) and (i % 5 == 0):
            result.append(i)
    return sum(result)

num1, num2 = map(int,input().split())
print(Calculation(num1,num2))