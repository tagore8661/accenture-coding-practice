"""
Write a Python function find_nearest_char(char_array, target_char) that takes a list of characters and 
a target character as inputs. The function should return the character from the list that is closest to 
the target character based on their ASCII values. If the target character is not a valid single alphabetic 
character, the function should return an error message.

Additionally, implement a program to:

Take a list of characters as input from the user.
Take a single character as the target character from the user.
Find and print the nearest character to the target character from the list.

Example:

Input : 
char_array_input = ["a", "b", "d", "e" , "f"]
target_char_input = "c"

Output :

The character nearest to 'c' is: b

"""


def find_nearest_char(char_array, target_char):
    # Ensure the target character is a valid single character input
    if len(target_char) != 1 or not target_char.isalpha():
        return "Invalid input. Please enter a single alphabetic character."
    
    # Sort the array to find the nearest character easily
    sorted_array = sorted(char_array)
    print(sorted_array)

    # Find the closest character using the minimum absolute difference in ASCII values
    nearest_char = min(sorted_array, key=lambda char: abs(ord(char) - ord(target_char)))

    return nearest_char

# Take user inputs
char_array_input = input("Enter characters separated by spaces: ").split()
target_char_input = input("Enter a single character to find the nearest: ")

# Find and print the nearest character
result = find_nearest_char(char_array_input, target_char_input)
print(f"The character nearest to '{target_char_input}' is: {result}")