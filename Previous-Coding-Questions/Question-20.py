"""
Chocolate Jar -

You are given an integer array of size N, representing jars of chocolates. Three students A, B, and C respectively, 
will pick chocolates one by one from each chocolate jar, till the jar is empty. and then repeat the same with the 
rest of the jars. Your task is to find and return an integer value representing the total number of chocolates that
student A will have, after all the chocolates have been picked from all the jars.

Note: Once a jar is done A will start taking the chocolates from the new jar.

Input Format:

input1: An integer array representing the quantity of chocolates in each jar.
input2: An integer value N representing the number of jars.

Output Format:

Return an integer value representing the total number of chocolates that student A will have, after all the chocolates are picked.

Example:

Input:
10 20 30
3
Output: 21

Explanation:

Jar 1: 20 chocolates -> A-4, B-3, C-3
Jar 2: 20 chocolates -> A-7, B-7, C-6
Jar 3: 30 chocolates -> A-10, B-10,C-10

so A gets a total of 4+7+10=21 chocolates.
"""


def total_chocolates_A(chocolate_jars, N):
    # Initialize total chocolates for student A
    total_chocolates_A = 0
    
    # Iterate over each jar in the list
    for chocolates in chocolate_jars:
        # While there are chocolates in the current jar
        while chocolates > 0:
            # Student A takes 1 chocolate if available
            if chocolates > 0:
                total_chocolates_A += 1
                chocolates -= 1
            
            # Student B takes 1 chocolate if available
            if chocolates > 0:
                chocolates -= 1
            
            # Student C takes 1 chocolate if available
            if chocolates > 0:
                chocolates -= 1
    
    return total_chocolates_A


# Example usage:
chocolate_jars = [10, 20, 30]
N = len(chocolate_jars)

result = total_chocolates_A(chocolate_jars, N)
print(f"Total chocolates picked by student A: {result}")