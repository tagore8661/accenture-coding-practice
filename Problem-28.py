#Counting Specified CHAR in a Given String

"""
You are given a string S of length N. Your friend wants to know the number of time his favorite 
letter C occurs in the string Your task is to help your finding and return an integer value 
representing the number of times a characte an particular string

input1 : helloworld
input2 : 10
input3 : l

Output : 3
"""

def char_count(str,char):
    count = 0
    for i in str:
        if i == char:
            count +=1
    return count

str,char = map(str,input().split())
print(char_count(str,char))