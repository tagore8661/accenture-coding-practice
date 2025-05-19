"""
Name Entry - 

Your friend has made entry of a name in the form first name F and last name L in your contact list. 
But some letters are in uppercase while others are in lowercase. Your task is fond and return a 
string representing the names such that the first name of Your contact is in lowercase, and the 
last name of your contact is in uppercase.

Input Specification:

Input1: A string F. representing the first name
input2: A string L representing the last name

Output Specification:

Return a string representing the names such that the first name of your contact is in lowercase,
and the last name of your contact is in uppercase.

"""

def format_name(F, L):
    # Convert the first name to lowercase
    first_name_lower = F.lower()
    
    # Convert the last name to uppercase
    last_name_upper = L.upper()
    
    # Combine and return the formatted name
    return first_name_lower + " " + last_name_upper

# Example usage:
input1 = "GanUgA"
input2 = "tAGoRE"
output = format_name(input1, input2)
print(f"Formatted Name: {output}")