"""You have to find and return the number between 'a' and 'b'
 ( range inclusive on both ends) which has the maximum exponent of 2."""

def Count(i):
    count = 0
    while i % 2 == 0 and i != 0:
        count +=1
        i //= 2
    return count

def MaxExponents(num1,num2):
    max,number = 0,num1
    for i in range(num1,num2):
        temp = Count(i)
        if temp > max:
            max ,number = temp , i
    return number


num1,num2 = map(int,input().split())

print(MaxExponents(num1,num2))