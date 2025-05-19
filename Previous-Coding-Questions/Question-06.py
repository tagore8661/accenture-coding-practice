"""
Special Fibonacci -

Alex is exploring a series and she came across a special series, in which

   f(N)=f(N-1)*f(N-1)+f(N-2)*f(N-2)
   where f(0) = 1, f(1) = 1

Your task is to help Alex find and return an integer value, representing the Nth number in this special series

Note: Return the output modulo 47.

Input Specification:

input1: An integer value N.

Output Specification:

Return an integer value, representing the Nth number in this special series.

Example1 :

input : 2
Output : 2
"""


def special_fibonacci(n):
    if n == 0 or n == 1:
        return 1

    # Initialize the first two values of the series
    a, b = 1, 1

    # Calculate up to the Nth value
    for _ in range(2, n + 1):
        c = (a * a + b * b) % 47 # (a **2+ b **2) % 47
        a, b = b, c

    return c  #b

# Example usage
N = 2
print(f"The {N}th number in the special Fibonacci series is: {special_fibonacci(N)}")




# Special Fibonacci Series

def special_fibonacci_series(n): 
    series = [0, 1, 1]
    for i in range(3, n): 
        series.append(series [i - 1] + series [i - 2] + series [i - 3])
    return series[:n]

n=int(input("Enter the number of terms to generate: "))

if n <= 0:
    print("Please enter a positive number.") 
else:
    result = special_fibonacci_series(n)

    print("Special Fibonacci series:")
    print(" ".join(map(str,result)))

# Fibonacci Series

def fibonacci(n):
    if n == 1:
        return 1
    
    count = 0 
    a, b = 0, 1 # count variable to track nth value 
    while count < n: 
        c = a+b # swap a and b values 
        a, b = b, c
        print(c, end=" ")
        count += 1

fibonacci(10) #1 2 3 5 8 13 21 34 55 89


# Factorial 

def fact (n):
    if n == 0:
        return 1
    else :
        factorial = 1
        for i in range(1,n +1):
            factorial *= i
        return factorial
n = fact(6)
print("\n Factorial =",n)