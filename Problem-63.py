"""
You are given a string array S that contains the names of some files along with their versions. 
Your task is to find and return an integer value representing the latest version out of all the 
flies that are correctly named in the array. A file is considered correct if it follows the 
format of the file named as "File_X" (where X represents the file version number). Return -1 
if there are no correct files in the array

Input 1: A string array S, representing the names of the files

Input2: An Integer value representing the size of the array

Output: Return an integer value
"""

def latest_version(S):
    latest = -1
    for file in S:
        parts = file.split('_')
        if len(parts) == 2 and parts [0] == "File" and parts [1].isdigit(): 
            version = int(parts[1]) 
            latest = max(latest, version)
    return latest

n = int(input())
S = list(map(str, input().split()))

print("Latest version:", latest_version(S))