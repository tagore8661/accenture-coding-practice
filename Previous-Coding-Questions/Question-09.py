"""
File Version -

You are given a string array S that contains the names of some files along with their To versions your task 
is to find and return an integer value representing the latest versions out of all the files that are 
correctly named in the armay. A file is considered correct if it follows the format of the file named as 
"File_X" (where X represents the file version number), Return-1 if there are no curect Files in the array

Note -
   A file is incorrect if the file does not match the format
   If there is no file in the files array then also return -1.

Input Specification :

Input1: A string array S, representing the names of the files.
Input2: An integer value representing the size of the array.

Output Specification:

Retum an integer value representing the latest version out of all the files that are correctly named in the array.

Example 1:

input1: {File_1,File_3,File_2}
input2: 3

Output: 3

"""

import re  # Import regular expression library for pattern matching

def latest_version(input1, input2):
    # input1: List of file names (S)
    # input2: Size of the array
    
    latest_version = -1  # Default value in case no correct files are found
    pattern = r"^File_(\d+)$"  # Regular expression for matching the format "File_X"
    
    # Loop through the array of file names
    for file in input1:
        match = re.match(pattern, file)  # Check if the file name matches the pattern
        
        if match:
            version = int(match.group(1))  # Extract the version number from the file name
            latest_version = max(latest_version, version)  # Update the latest version if necessary
    
    return latest_version

# Example:
input1 = ["File_1", "File_3", "File_2"]
input2 = 3

print(latest_version(input1, input2))




def find_latest_version(file_names, size):
    max_version = -1
    
    for file in file_names:
        if file.startswith("File_"):
            try:
                version = int(file.split("_")[1])  #int(file[5:])
                if version > max_version:
                    max_version = version
            except ValueError:
                continue
    
    return max_version

# Example usage
file_names = ["File_1", "File_3", "File_2"]
size = 3

print(f"Latest version: {find_latest_version(file_names, size)}")