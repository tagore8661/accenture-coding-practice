"""
Rebound Height -

Daniel has a ball He wants to find the bai's rebound height, which he dropped from height H with an initial velocity V. 
After the Nth rebound the final velocity of the ball is Vn Your task is to help him find and return an integer value 
representing the height to which the ball rebounds after N bounces.

Note -
   H'= H * e 2n, where H' & the rebound height. H is the initial height, e is the coefficient of restitution and is 
   the number of bounces
   e n = V/Vn ,where V is the initial velocity and Vn is the final velocity

Input Specification:

input1: An integer H, representing initial height
input2: An integer V, representing initial velocity
input3: An integer V, representing final velocity

Outnut Snecification:

Return an integer value representing the height to which the ball rebounds after N bounces.

Example1:

input1 : 10
input2 : 20
input3 : 5

Output : 160
"""

def rebound_height(H, V, Vn):
    # Calculate the coefficient of restitution
    e_n = V / Vn
    
    # Calculate the rebound height
    rebound_height = H * (e_n ** 2)
    
    return int(rebound_height)

# Example usage
H = 10  # initial height
V = 20  # initial velocity
Vn = 5  # final velocity

print(f"The rebound height after N bounces is: {rebound_height(H, V, Vn)}")