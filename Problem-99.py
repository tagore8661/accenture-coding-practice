"""
Parking Lot -

The function accepts a character array 'arr' of size 'n' as its argument. Each element of 'arr' represents the status of a parking slot, 
where 'S' represents an empty slot and 'X' represents an occupied slot. The function needs to return the maximum number of cars that can 
be parked in the parking lot. It is assumed that two cars cannot occupy the same slot and cars can only park in consecutive empty slots.

Example:

Input:
n: 16
arr: XXXSXXSXXSSXXSXX

Output:
7

"""

def max_cars_parked(n, arr):
    max_cars = 0
    current_cars = 0

    for status in arr:
        if status == 'S':
            current_cars += 1
        else:
            max_cars = max(max_cars, current_cars)
            current_cars = 0

    max_cars = max(max_cars, current_cars)
    return max_cars

n = 16
arr = "XXXSXXSXXSSXXSXX"
result = max_cars_parked(n, arr)
print(result)