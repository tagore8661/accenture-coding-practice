"""The function accepts 3 positive integers 'a' , 'b' and 'c ' as its arguments. 
Implement the function to return.

( a+ b ) , if c=1
( a - b ) , if c=2
( a * b ) ,  if c=3
(a / b) ,  if c =4"""

def Operation(c,a,b):
    if c == 1:
        return (a + b)
    elif c == 2:
        return (a - b)
    elif c == 3:
        return (a *  b)
    else:
        return (a // b)
c,a,b = map (int,input().split())
print(Operation(c,a,b))