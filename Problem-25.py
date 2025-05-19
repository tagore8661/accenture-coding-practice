"""To solve this problem, we need to write a Python function that 
finds the word from a given dictionary 'D' that rhymes best with a given string 'S'.
A word rhymes best if it shares the longest suffix with 'S'.
If no word rhymes, we should return "No Word"."""

"""A poet has asked you for assistance in writing poems. 
He has given you a string S and a dictionary D and he asks you to find, from the dictionary, 
a word which rhymes best with S. Words are said to rhyme when the last syllables of the words are the same, 
like "cave" and "gave", or "typical" and "critical. 
The words will be deemed to rhyme best if the last few characters of the words match the most

Your task is to find and return a string value denoting the word which rhymes best with S, from the dictionary D. 
If no such word is found return the string "No Word".  """

def find_rhyming_word(S, D):
    # Initialize variables to keep track of the best rhyming word and maximum suffix length
    best_rhyme = "No Word"
    max_suffix_length = 0

    # Iterate through each word in the dictionary D
    for word in D:
        # Check the length of the smaller word (between S and the word from D)
        max_possible_suffix = min(len(S), len(word))

        # Find the longest suffix match for the current word
        for i in range(1, max_possible_suffix + 1):
            # Check if the suffixes of length i match
            if S[-i:] == word[-i:]:
                # If a longer matching suffix is found, update the best rhyme
                if i > max_suffix_length:
                    max_suffix_length = i
                    best_rhyme = word
            else:
                # If a mismatch is found, stop checking further for this word
                break

    return best_rhyme

# Example usage
"""S = "gave"
D = ["save","cave","have", "wave", "crave"] """
S = "thunder"
D = ["puzzle","thunder","powder","blender","under"]
print(find_rhyming_word(S, D))  # Output should be "cave" as it rhymes best with "gave"



#Another Way

def find_rhyming_word(S, D):
    """
    Finds the best rhyming word from the dictionary.

    Args:
        S: The word to find a rhyme for.
        D: The dictionary of words.

    Returns:
        The best rhyming word from the dictionary, or "No Word" if none is found.
    """

    # Find the last syllable of the input word
    last_syllable = S.split()[-1]

    # Iterate through the dictionary words and find the best match
    best_match = None
    best_match_length = 0
    for word in D:
        last_word_syllable = word.split()[-1]
        if last_word_syllable[-len(last_syllable):] == last_syllable:
            if len(last_word_syllable) > best_match_length:
                best_match = word
                best_match_length = len(last_word_syllable)

    # Return the best match or "No Word"
    if best_match:
        return best_match
    else:
        return "No Word"

# Example usage
S = "gave"
D = ["save","cave","have", "wave", "crave"]

print(find_rhyming_word(S, D))