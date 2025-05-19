"""You are developing a feature for an environmental awareness app that helps users to know how much area their tree's shadow covers.
You have the distance tree's trunk to the edge D from a of the shadow.
Your task is to calculate and return an integer value representing the shadow area of the canopy."""

import math

def calculate_shadow_area(D):
    # Calculate the area of the shadow
    shadow_area = math.pi * (D ** 2)
    # Return the area as an integer
    return int(shadow_area)

# Example usage
D = int(input())  # Distance from the tree trunk to the edge of the shadow
shadow_area = calculate_shadow_area(D)
print(f"The shadow area of the canopy is: {shadow_area} square units")



"""Another Simple Way"""
a = int(input())
area = 3.14*a*a
print(round(area))