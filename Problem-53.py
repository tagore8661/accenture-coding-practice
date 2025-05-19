"""
Alice has a peculiar fondness for strings without any interruptions. She considers"." as an interruption. 
You are given a string S and your task is to find and return the length of the longest uninterrupted 
substring to match alices fondness.

"""

"""def longest_uninterrupted_substring(s):
    max_length = 0
    current_length = 0
    
    for char in s:
        if char != '.':
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
    
    # Final check after the loop
    if current_length > max_length:
        max_length = current_length
    
    return max_length

# Example usage:
s = "abc.def.ghi.jkl"
print(longest_uninterrupted_substring(s))  #Output: 3 """

s = "abc.de.f"
arr = s.split(".")

max_length = 0

for strr in arr:
    if len(strr) > max_length:
        max_length = len(strr)
print(max_length)