"""
Halloween Candies -
Bob goes to super market to shop candies represented by an array A for halloween party, his mother gave him some money M. 
Due to the festive season, there are several offers in the supermarket. One such offer useful for Bob is, if the price of 
the candy is a multiple of 5, he can buy it without spending any money otherwise he will spend money equal to Ai which is 
the price of a particular candy. Bob can shop as long as he has money. Your task is to find and return the maximum number 
of candies Bob can buy.

Note: Assume 1-based indexing.

Input Specification:

input1: An integer value, representing number of candies. 
input2: An integer array A, representing price of each candy. 
input3: An integer value M, representing the amount of money.

Output Specification:
Return the number of candies Bob can buy.

Example 1 :

input1 : 3
input2 : [5,5,105]
input3 : 16
"""


def max_candies(num_candies, prices, money):
    candies_bought = 0
    
    for price in prices:
        if price % 5 == 0 & money >= price :
            candies_bought += 1
        elif money >= price:
            money -= price
            candies_bought += 1
    
    return candies_bought

# Example usage
num_candies = 3
prices = [5, 5, 105]
money = 16

print(f"Maximum number of candies Bob can buy: {max_candies(num_candies,prices, money)}")


"""
def max_candies(input1, input2, input3):
    # input1: Number of candies
    # input2: List of candy prices
    # input3: Amount of money M
    
    num_candies = input1  # Number of candies
    candy_prices = input2  # Prices of candies
    money = input3  # Total money M
    
    candy_count = 0  # Count of candies Bob can buy
    
    # Loop through the list of candies
    for i in range(num_candies):
        price = candy_prices[i]
        
        # Check if the price is divisible by 5 (Bob can take it for free)
        if price % 5 == 0 & money >= price:
            candy_count += 1  # Bob gets the candy without spending money
        else:
            # If Bob has enough money, he can buy the candy
            if money >= price:
                candy_count += 1  # Bob buys the candy
                money -= price  # Deduct the money spent on this candy
            else:
                # If Bob doesn't have enough money, he can't buy any more candies
                break
    
    return candy_count

# Example:
input1 = 3
input2 = [5, 5, 105]
input3 = 16

print(max_candies(input1, input2, input3))
"""