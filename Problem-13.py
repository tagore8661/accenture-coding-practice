"""The function accepts a string “str” of length ‘n’, that contains alphabets and hyphens (-).
 Implement the function to move all hyphens(-) in the string to the front of the given string"""

inp = input()
count = 0
str = ""
for i in inp:
    if i == "_" :
        count +=1
    else :
        str += i
print("_"*count,str)