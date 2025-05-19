"""
Write a Code, that takes a string s as input and returns the length of the longest substring with 
all unique characters. A substring is a contiguous sequence of characters within a string.

For example, in the string "abcabcbb", the longest substring with unique characters is "abc", 
which has a length of 3. The function should use a list to track the characters that have 
already been encountered in the current substring.

"""
def longestUniqueSubstr(s): 
    n = len(s) 
    res = 0

    for i in range(n):

        visited = [False] * 256
        for j in range(i, n):

            if visited[ord(s[j])] == True: 
                break

            else: 
                res = max(res, j - i + 1) 
                visited[ord(s[j])] = True

    return res

if __name__ == "__main__": 
    s = "abcabcbb"
    print(longestUniqueSubstr(s))