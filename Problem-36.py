#YT_Techie CodeBuddy

"""Problem Statement: (18 Sept 2023)

Given a number N your Task is to make N a single digit number by performing these operations

1) If N is odd, make it floor (N/2)

2) If N is even, make it floor((N-2)/2)

3) If N is already a single digit, print as it is

Example:

Input 1: N=25

Output 1: 12

Input 2: N=10

Output 2: 4

Input 3: N=5

Output 3: 5 """

import math
N = int(input())
while N > 9:
    if N % 2 == 0:
        N = math.floor(N /2)
        break
    else:
        N = math.ceil((N-2)/ 2)
        break


print(N)  # Output will be the modified single-digit number