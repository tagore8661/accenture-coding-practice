#Replace Characters in given string

# Input string
s = input()

# Input characters to be replaced
ch1 = input().strip()
ch2 = input().strip()

# Resultant string after replacement
res = ""
for c in s:
    if c == ch1:
        res += ch2
    elif c == ch2:
        res += ch1
    else:
        res += c

print(res)