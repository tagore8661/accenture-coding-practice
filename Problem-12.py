# writing numbers that uses only n different symbols

def NumChar(num,n):
    reminder = []
    quotient = num // n
    reminder.append(num%n)
    while quotient != 0:
        reminder.append(quotient % n)
        quotient //=n
    
    reverse_reminder= reminder[::-1]
    result=" "
    for i in reverse_reminder:
        if i > 9:
            a = i -9
            a +=64
            result += chr(a)
        else:
            result +=str(i)
    return result

num = int(input())
n = int(input())

print(NumChar(num,n))


"""n = int(input())
num = int(input())
reminder = []
quotient = num // n
reminder.append(num%n)
while quotient != 0:
    reminder.append(quotient%n)
    quotient = quotient // n
reminder = reminder[::-1]
equivalent = ''
for i in reminder:
    if i > 9:
        a = i - 9
        a = 64 + a
        equivalent+=chr(a)
    else:
        equivalent+=str(i)
print(equivalent)"""