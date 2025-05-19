"""You have a basket full of apples and mangoes, your job is to make the numer of apples 
and given a function that accepts three integers 'a', 'm' and 'rs' as its argument where 
'a' and a basket respectively and 'rs' is the rupees that you have. Implement the function 
to balance the basket.

If 'a' > 'm', then buy (a - m) mangoes at the rate of Rs 1 per mango.

If 'a' < 'm', then sell (m - a) mangoes at the rate of Rs 1 per mango.

Return the total rupees left with you after balancing the fruits."""

def Balancefruits(a,m,rs):

    if a>m:

        b=a-m

        total=rs-b

        return total

    else:

        c=m-a

        total=rs-c

        return total

x=Balancefruits(int(input()),int(input()),int(input()))

print(x)