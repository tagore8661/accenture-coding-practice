"""
Island Life -

You are stuck on an island where they sell and eat coconut sweets only. A person can buy at most 1 box 
per day with each box containing N pieces. To remain alive you must consume E coconut sweets daily for 
D days, but the catch is you cant purchase sweets on sundays. Your task is to find and return an integer 
value representing the minimum number of times you have to buy coconut sweets in order to stay alive. 
If not possible, return -1

Note: The day starts from Monday

Input Specification:

input1: An integer value N. representing the number of coconut sweets per box
input2: An integer value E. representing the number of coconut sweets you must eat daily
input3: An integer value D. representing the days ypu have to spend on the on island

Output Specification:

Return an integer value representing the minimum number of times you have to buy coconut sweets in order 
to stay alive. If not possible, return -1

Explanation :

input1 = 10  # N = 10 sweets per box
input2 = 5   # E = 5 sweets needed daily
input3 = 10  # D = 10 days on the island

Total sweets needed = E * D = 5 * 10 = 50 sweets.
Number of Sundays = D // 7 = 10 // 7 = 1 Sunday.
Buying days available = D - number_of_sundays = 10 - 1 = 9 days.
Boxes needed = ceil(total_sweets_needed / N) = ceil(50 / 10) = 5 boxes.
Check if possible: Since you have 9 buying days and need to buy 5 boxes, it is possible.

Output: 5 (minimum purchases).
"""

import math

def min_purchases(N, E, D):
    # Total sweets needed to survive for D days
    total_sweets_needed = E * D
    
    # Calculate number of Sundays (non-buying days)
    number_of_sundays = D // 7
    
    # Calculate total buying days (i.e., days when you can buy sweets)
    total_buying_days = D - number_of_sundays
    
    # Calculate how many boxes you need to buy
    boxes_needed = math.ceil(total_sweets_needed / N)
    
    # Check if it's possible to buy enough boxes in the available days
    if boxes_needed <= total_buying_days:
        return boxes_needed
    else:
        return -1

# Example usage:
input1 = 10  # N: Number of sweets per box
input2 = 5   # E: Daily requirement of sweets
input3 = 10  # D: Number of days on the island
output = min_purchases(input1, input2, input3)
print(f"Minimum purchases: {output}")