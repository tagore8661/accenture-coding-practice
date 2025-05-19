"""
Write a Python function number_to_words(num) that converts a given integer less than 1000 
into its alphabetical word representation.

Example:

Input: 999 
Output: Nine Hundred and Ninety Nine
"""


# Function to convert numbers to words
def number_to_words(num):
    # Dictionaries for numbers and their word equivalents
    ones = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
        6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
        15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
    }

    tens = {
        20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
        60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
    }
    
    if num < 20:
        return ones[num]  # Numbers from 0 to 19 have direct mappings
    elif num < 100:
        # Tens place + ones place
        return tens[num // 10 * 10] + ('' if num % 10 == 0 else ' ' + ones[num % 10])
    elif num < 1000:
        # Hundreds place + recursion for the remaining part
        return ones[num // 100] + ' Hundred' + ('' if num % 100 == 0 else ' and ' + number_to_words(num % 100))

# Take user input
num = int(input("Enter a number less than 1000: "))

if 0 <= num < 1000:
    print(number_to_words(num))
else:
    print("Please enter a number less than 1000.")