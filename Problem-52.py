"""
In a tech startup, the team faced a software bug the zeros in their data outputs were causing their system to crash.
 A junior developer suggested replacing all the O's with 5's as a quick fix. By implementing this simple code tweak,
they stabilized the system. Your task is to find and return an integer value representing the value that stabilizes the system.

Input Specification:
input1: An integer value

Output Specification:
Return an integer value representing the value that stabilizes the system
"""

"""def stabilize_system(input1):
    stabilized_value = str(input1).replace('0', '5')
    return int(stabilized_value)

# Example usage:
input1 = 102030
print(stabilize_system(input1))  # Output will be 152535 """


def stabilize_system(input_string):
    result = ""
    for char in input_string:
        if char == '0':
            result +='5'
        else :
            result +=char
    return result
input_string = "102030"
print(stabilize_system(input_string))