#longest string

def getLongestString(s):
    l = s.split()
    maxi = 0 
    ans = None
    for word in l:
        if len(word) > maxi:
            ans = word 
            maxi = len(word)
    return ans 

s = input()
print("The longest string is:", getLongestString(s))