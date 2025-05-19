"""
In a remote village, there existed two mystical strings S1 and S2. In these strings was
 hidden a secret encoded in their characters. 
 Your task is to find and return an integer value representing the encoded secret of the
 strings by finding the sum of the ASCII values of the characters in the longest common 
 substring between these two Strings Return 0 if there 150 common substring.
"""

def longest_common_substring(S1, S2):
    m, n = len(S1), len(S2)
    # Create a 2D array to store lengths of longest common suffixes
    lcsuff = [[0] * (n + 1) for _ in range(m + 1)]
    length = 0  # Length of the longest common substring
    row, col = 0, 0  # To store the ending point of the longest common substring

    # Building the lcsuff array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                lcsuff[i][j] = lcsuff[i - 1][j - 1] + 1
                if lcsuff[i][j] > length:
                    length = lcsuff[i][j]
                    row, col = i, j
            else:
                lcsuff[i][j] = 0

    # If there is no common substring
    if length == 0:
        return 0

    # Retrieve the longest common substring
    longest_common_substr = ""
    while lcsuff[row][col] != 0:
        longest_common_substr = S1[row - 1] + longest_common_substr
        row -= 1
        col -= 1

    # Calculate the sum of ASCII values of the characters in the longest common substring
    ascii_sum = sum(ord(char) for char in longest_common_substr)
    return ascii_sum

# Example usage:
S1 = "abcde"
S2 = "abfce"
print(longest_common_substring(S1, S2))  # Output will be 195 (for the substring "ab")