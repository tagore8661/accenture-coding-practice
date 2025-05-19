"""
Substring Search 

The function accepts two strings 'str1' and 'str2' as its argument. The function needs to return the index of the 
first occurrence of substring 'str2' in string 'str1' or -1 if the substring is not found.

Example:

Input:
str1: “Hello, World!”
str2: “World”
 	 	
Output:
7
"""

def substring_search(str1, str2):
    index = str1.find(str2)
    return index if index != -1 else -1

str1 = "Hello, World!"
str2 = "World"
print(substring_search(str1, str2))