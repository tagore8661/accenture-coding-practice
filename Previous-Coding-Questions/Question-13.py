"""
Canopy Area -

You are developing a feature for an environmental awareness app that helps users to know how much 
area their tree's shadow covers. You have the distance D from a tree's trunk to the edge of the shadow. 
your task is to calculate and return an integer value representing the shadow area of the canopy

Note - Round off the result to nearest integer.

Input Specification:

input1: An integer value D, representing the distance from the tree trunks to the edge of shadow.

Output Specification:

Retum an integer value representing the shadow area of the canopy.

Example 1:

Input1:5
Output: 78

Explanation:

Here, D = 5,So area of the canopy would be 3.14*5*5=78.5,Therefore 78 will be returned as output.
"""

import math

def canopy_area(D):
    # Calculate the area of the canopy (circle area)
    area = math.pi * D**2
    
    # Round off to the nearest integer
    return round(area)

# Example usage
input1 = 5  # D = 5 units
output = canopy_area(input1)
print(f"Canopy area: {output}")