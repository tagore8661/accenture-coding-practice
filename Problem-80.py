"""
Rob has gone to Mars to collect some stones. The bag he carries can hold a maximum weight of M. 
There are M stones weighing from 1 to M on Mars. There are N stones on Mars that are similar 
to the ones on Earth. Find the number of stones he can bring from Mars such that none are 
similar to any stone on Earth.

Input Specification:
Input 1: M is the size of the bag and the number of different stone weights present on Mars.
Input 2: N is the number of common stones on Earth and Mars.
Input 3: An N elements array containing the list of the weights of the common stones

Example:

Input 1:10 (Bag size)
Input 2:3 (Common stones)
Input 3: [1,6,8]

[2,3,4,5,7,9,10]

2,3,4   2,3,5

Output: 3
"""

def get_unique_stones_to_bring(M, N, common_stones):
    #different weights present on Mars 
    mars_weights = list(range(1, M + 1))

    #weights already present on Earth 
    earth_weights = common_stones

    # unique arrays of mars and earth weights 
    mars_set = set(mars_weights) 
    earth_set = set(earth_weights)

    # unique weights present on mars but not on earth 
    unique_mars_weights = list(mars_set - earth_set)

    #sort the unique array in ascending order 
    unique_mars_weights.sort()

    # select stones from the Mars until bag capacity is reached
    total_weight = 0 
    num_stones_selected = 0

    for weight in unique_mars_weights:
        if total_weight + weight <=M:
            total_weight += weight
            num_stones_selected += 1
        else :
            break
    return num_stones_selected

#user input
input1 = int(input("Enter the capasity of Rob's bag : "))
input2 = int(input("Enter number of common stones on earth : "))
input3 = list(map(int,input("list of stones from earth : ").split()))
#function call
output = get_unique_stones_to_bring(input1,input2,input3)
print(output)