

def CountDigitOccurrences(l, u, x):
    # Initialize a variable to keep track of the total occurrences of digit x
    count = 0
    
    # Convert x to a string to facilitate comparison with digits in numbers
    x_str = str(x)
    
    # Loop through each number in the range [l, u]
    for number in range(l, u + 1):
        # Convert the current number to a string
        num_str = str(number)
        
        # Count how many times x_str appears in num_str
        count += num_str.count(x_str)
    
    # Return the final count
    return count

result = CountDigitOccurrences(10, 20, 1)
print(result)  # Output should be the number of times the digit '1' appears between 10 and 20