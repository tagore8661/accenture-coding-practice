"""You are provided with a string which has a sequence of 1's and 0's
This sequence is the encoded version of a English word. You are supposed 
write a program to decode the provided string and find the original word.
Each alphabet is represented by a sequence of 1s.

This is as mentioned below.

A:1

8:11

C:111

D:1111

E:11111

F:111111

and so on upto Z having 26 1's (11111111111111111111111111)"""

def binary_to_letter(str):
    result = ""
    count =0
    for i in str:
        if i == '1':
            count +=1
        else :
            if count > 0 :
                result += chr(64+count)
                count = 0
    if count > 0 :
        result += chr(64 + count)
    return result

str = input()
print(binary_to_letter(str))