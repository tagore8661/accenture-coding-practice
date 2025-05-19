"""
Daniel has a ball. He wants to find the ball's rebound height, which he dropped from height H with an initial velocity V.
After the Nth rebound the final velocity of the ball is Vn. Your task is to help him find and return an integer value 
representing the height to which the ball rebounds after N bounces.

Note:

H' = H x e²n, where H' is the rebound height, H is the initial height, e is
the coefficient of restitution and is the number of bounces

e" = V/Vn, where V is the initial velocity and V is the final velocity

Input Specification:

input1: An integer H, representing initial height
input2: An integer V, representing initial velocity
input3: An integer V., representing final velocity

Example 1:
input1: 10
input2: 20
input3: 5

Output: 160
"""

def fun1(in1, in2, in3):
    #int in1 - initial height
    #int in2 - initial velocity
    #int in3 - final velocity
    # this was given in the coding area

    e = in2//in3
    new_e = e**2
    return in1*new_e

print(fun1(10,20,5))


def fun2(in1, in2, in3):
    # int in1 - initial height
    # int in2 - initial velocity
    # int in3 - final velocity
    # this was given in the coding area

    e = in2 / in3

    new_e = e ** 2
    rebound_height = in1 * new_e  # at this point, the rebound height is a float.

    return int(rebound_height)  # return "an integer value representing the height"

print(fun2(10,20,5))