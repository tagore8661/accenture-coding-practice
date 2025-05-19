"""
Write a Code, that checks whether a given integer n is a power of 3. If n is a power of 3, 
the function should return "power of 3". Otherwise, it should return "not power of 3". Note 
that any value of n less than or equal to 0 should immediately return "not power of 3".
"""

def is_power_of_three(n): 
    if n <= 0: 
        return "not power of 3"

    while n % 3 == 0:
        n /= 3

    return "power of 3" if n == 1 else "not power of 3"

print(is_power_of_three(27)) 
print(is_power_of_three(81))