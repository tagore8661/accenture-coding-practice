"""
Bob goes to super market to shop candies represented by an array A for halloween party, 
his mother gave him some money M. Due to the festive season, there are several offers in the supermarket. 
One such offer useful for Bob is, if the price of the candy is a multiple of 5, he can buy it without 
spending any money otherwise he will spend money equal to Ai which is the price of a particular candy. 
Bob can shop as long as he has money. Your task is to find and return the maximum number of candies Bob can buy.

Note: Assume 1-based indexing.
"""

"""def max_candies(A, M):
    candies_bought = 0
    for price in A:
        if price % 5 == 0:
            candies_bought += 1
        elif M >= price:
            M -= price
            candies_bought += 1

    return candies_bought

# Example usage:
A = [5,6,7,10,12,15]
M = 20
print(max_candies(A, M))  # Output: 10 """


def max_candies (A, M):
    A.sort()
    count = 0
    for price in A:
        if price % 5 == 0:
            count += 1
        elif price <= M:
            count += 1
            M -= price
    return count
# Test case
A = [5, 10, 12, 15, 7, 6]
M = 20

print(max_candies (A, M)) # Output: 5