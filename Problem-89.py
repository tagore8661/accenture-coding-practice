#Write a program to find if the given number is prime or not.

num = int(input("enter a number: "))
# input: 23
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
# 23 is a prime number