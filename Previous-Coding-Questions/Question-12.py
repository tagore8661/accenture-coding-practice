"""
Poet and Rhymes -

A poet has asked you for assistance in writing poems. He has given you a string S and a dictionary D 
and he asks you to find, from the dictionary, a word which rhyme best with S. Words are said to rhyme 
when the last syllables of the words are the same, like "cave" and "gave", or "typical" and "critical." 
The words will be deemed to rhyme best if the last few characters of the words match the most.

Your task is to find and return a string value denoting the word which rhymes best with S, from the 
dictionary D. If no such word is found, return the string "No Word"

Note:
   • If all the characters match, it is the same word and not a rhyming word.
   • All the given words are in lowercase.
   • If multiple rhyming words are found, then choose the word with the least index

Input Specification:

input1: A string value S, representing a single word
input2: A string array D, representing the dictionary
input3: An integer value representing the length of array D

Output Specification:

Return a string value denoting the word which rhymes best with S from the dictionary D. If no such 
word is found, return the string "No Word".

Explanation:

Input:
S = "gave"
D = ["save", "wave", "cave", "rave", "gave", "brave"]
Steps:
We loop through each word in D:
"save": The last two characters "ve" match, so the suffix length is 2.
"wave": The last two characters "ve" match, so the suffix length is 2.
"cave": The last two characters "ve" match, so the suffix length is 2.
"rave": The last two characters "ve" match, so the suffix length is 2.
"gave": This is the same word as S, so it is skipped.
"brave": The last two characters "ve" match, so the suffix length is 2.
All words have a matching suffix length of 2, but "save" appears first in the list, so it is selected as the best rhyme.

Output:
Best rhyme: save
"""


def find_best_rhyme(S, D, N):
    best_match = None
    max_suffix_length = 0
    
    for word in D:
        if word == S:
            continue  # Skip if the word is exactly the same as S
        
        # Find the longest matching suffix
        suffix_length = 0
        min_len = min(len(S), len(word))
        
        for i in range(1, min_len + 1):
            if S[-i] == word[-i]:
                suffix_length += 1
            else:
                break
        
        # Update the best match if this word has a longer matching suffix
        if suffix_length > max_suffix_length:
            best_match = word
            max_suffix_length = suffix_length
    
    # If no match found, return "No Word"
    if best_match is None:
        return "No Word"
    
    return best_match

# Example usage:
input1 = "gave"  # S
input2 = ["save", "wave", "cave", "rave", "gave", "brave"]  # D
input3 = len(input2)  # Length of D
output = find_best_rhyme(input1, input2, input3)
print(f"Best rhyme: {output}")


"""
def find_best_rhyme(S, D):
    best_word = ""
    max_length = 0
    
    for word in D:
        if word == S:
            continue  # Skip if the word is the same as S
        
        # Find the length of the matching suffix
        match_length = 0
        min_length = min(len(S), len(word))
        
        for i in range(1, min_length + 1):
            if S[-i] == word[-i]:
                match_length += 1
            else:
                break
        
        # Update best match if this word has a longer matching suffix
        if match_length > max_length:
            best_word = word
            max_length = match_length
            
    return best_word if best_word else "No Word"

# Example usage
S = "cave"
D = ["brave", "gave", "save", "wave", "cave"]
print(find_best_rhyme(S, D))  # Output: "No Word"

"""