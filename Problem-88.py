#Write a program to print the given number is odd or even.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


#Write a program to find the given number is positive or negative.

num = float(input("Enter a number: "))
# Input: 1.2
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

#output: Positive number