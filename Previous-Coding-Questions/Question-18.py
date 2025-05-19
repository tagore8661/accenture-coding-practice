"""
Stabilize the System -

In a tech startup, the team faced a software bug the zeros in their data outputs
were causing their system to crash. A junior developer suggested replacing all 
the O's with 5's as a quick fix. By implementing this simple code tweak, they 
stabilized the system. Your task is to find and return an integer value representing 
the value that stabilizes the system.

Input Specification:

input1: An integer value

Output Specification:

Return an integer value representing the value that stabilizes the system

Example 1:

input1: 100067
Output: 155567

input2: 12345
Output2: 12345
"""

def stabilize_system(input1):
    # Step 1: Convert the integer to a string
    input_str = str(input1)
    
    # Step 2: Replace all '0' with '5'
    stabilized_str = input_str.replace('0', '5')
    
    # Step 3: Convert the string back to an integer and return
    return int(stabilized_str)


# Example usage:
input1 = 100067  # Given input
output = stabilize_system(input1)
print(f"Stabilized value: {output}")