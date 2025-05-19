# Return the number of carries of addition of two integer 

def numberOfCarries(num1,num2):
    l1 =len(num1)
    l2 =len(num2)
    
    carry = 0
    count = 0
    while (l1 != 0 or l2 != 0):
        x= 0
        y=0

        if(l1 > 0):
            x = int(num1 [l1 -1])
            l1 -= 1

        if(l2 > 0):
            y = int(num2[l2 -1])
            l2 -= 1

        sum = x + y + carry
 
        if sum > 9 :
            carry = 1
            count += 1

        else :
            carry = 0

    return count
num1 = input()
num2 = input()

print(numberOfCarries(num1,num2))