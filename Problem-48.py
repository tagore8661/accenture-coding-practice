"""
4) Check the number of Char occurance in a string.

Sample input : g.Tagore

char : g

Output : 2
"""

def count_char_occurrences(s, char):
    # Use the count method to count occurrences of the character
    return s.count(char)

# Example usage:
s = "g.Tagore"
char = 'g'
print(count_char_occurrences(s, char))  # Output will be 2