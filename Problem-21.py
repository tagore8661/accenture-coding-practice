"""Write a program in C such that it takes a lower limit and upper limit as inputs 
and print all the intermediate palindrome numbers."""

def Num_Palindrome(num1,num2):
    values =[]
    for i in range(num1,num2):
        string = str(i)
        reverse = string[::-1]

        if i == int(reverse) :
            values.append(i)

    return values
num1 = int(input())
num2 = int(input())

print(Num_Palindrome(num1,num2))