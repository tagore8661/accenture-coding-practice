"""
Sum of Leap Years in a Range -

Write a program that takes two positive integers startYear and endYear as input. The
program should calculate the sum of all leap years between startYear and endYear
(both inclusive) using a while loop and print the result.

"""

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

startYear = int(input("Enter start year: "))
endYear = int(input("Enter end year: "))
total = 0
year = startYear
while year <= endYear:
    if is_leap_year(year):
        total += year
    year += 1
print("Sum of leap years:", total)
