"""Write a program in C to display the table of a number and print the sum of all the multiples in it."""

def Sum_Multiple(n):
    sum = 0

    for i in range(1,11):
        value = i * n
        print(value ,end=",")
        sum += value

    return sum

num = int(input())
print("\n SUM OF MULTIPLE",Sum_Multiple(num))