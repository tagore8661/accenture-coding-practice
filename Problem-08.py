#CheckPassword

def Check_Password (str,n):
    if n < 4 :
        return 0
    if str[0].isdigit():
        return 0
    num =0
    cha =0
    for i in range(n):
        if str[i] == " " or str[i] == "/" :
            return 0
        if str[i] >= "A"  and str[i] <= "Z":
            cha +=1

        elif str[i].isdigit():
            num +=1

    if cha > 0 and num > 0:
        return 1
    else :
        return 0
    
str = input()
n = len(str)

print(Check_Password(str,n))