"""
Financial Dataset - 		
 
You are workirg on a financtal analyzing tool which represents the daily stock prices of a
company over a time. Each element in an integer array A of size N represents the closing 
price of the stock for a particular day. Your task is to find and return an integer value
representing the total number of days where the stock price decreased indicating negative growth.

Input Specification :

input1 : An Integer array A containing the closing price of the stock. 
input2 : An integer value N representing the size of array

Output Specification:

Return an integer value representing the total number of days where the stock price
decreased,indicating negative growth.

Example 1:
A = [100, 98, 105, 103, 101, 120, 115]
Output: 4

Example 2:
A = [150, 155, 160, 165]
Output:0

Example 3:
A = [200, 195, 210, 190, 180, 170]
Output: 4




"""

def count_negative_growth_days(A, N):
    # Initialize counter for negative growth days
    negative_days = 0

    # Iterate through the array from the second day to the last day
    for i in range(1, N):
        # If current day's price is less than the previous day's price, it's negative growth
        if A[i] < A[i - 1]:
            negative_days += 1

    return negative_days


# Example usage:
A = [100, 98, 105, 103, 101, 120, 115]
N = len(A)
result = count_negative_growth_days(A, N)
print(f"Total number of days with negative growth: {result}")