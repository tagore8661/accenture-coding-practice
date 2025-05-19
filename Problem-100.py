#Write a program to print the following pattern.
"""
*
* *
* * *
* * * * 
* * * * * 
"""
def myfunc(n):
	for i in range(0, n):
		for j in range(0, i+1):
			print("* ",end="")
		print("\r")

n = 5
myfunc(n)


#Write a program to print the following pattern.
"""
        * 
      *   *  
    *   *   * 
  *   *   *   * 
*   *   *   *   *

"""
def myfunc(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
n = 5
myfunc(n)


#Write a program to print the following pattern.
"""
1
1 2 
1 2 3 
1 2 3 4
1 2 3 4 5
"""
def num(n):
	num = 1
	for i in range(0, n):
		num = 1
		for j in range(0, i+1):
			print(num, end=" ")
			num = num + 1
		print("\r")
n = 5
num(n)


#Write a program to print the following pattern.
"""
1
2 3 
4 5 6 
7 8 9 10
11 12 13 14 15
"""
def num(n):
	num = 1
	for i in range(0, n):
		for j in range(0, i+1):
			print(num, end=" ")
			num = num + 1
		print("\r")

n = 5
num(n)


#Write a program to print the following pattern.
"""
A
B B
C C C
D D D D
E E E E E
"""
def alphapat(n):
	num = 65
	for i in range(0, n):
		for j in range(0, i+1):
			ch = chr(num)
			print(ch, end=" ")
		num = num + 1
	
		print("\r")
n = 5
alphapat(n)


#Write a program to print the following pattern.
"""
A
B C
D E F 
G H I J
K L M N O
"""
def contalpha(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=" ")
            num = num + 1
        print()
n = 5
contalpha(n)