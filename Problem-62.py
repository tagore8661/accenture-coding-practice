"""
Problem Statement:

A young boy finds it difficult to read words that are more than 10 letters long. 
To help him, you need to write a program that shortens such words. Specifically, 
for any word longer than 10 letters, the program should convert it into a format where only the first letter, 
the number of letters in between, and the last letter are kept. For example, the word "demonstration" becomes "dlln".

Your task is to implement a program that will take a sentence as input and produce a modified sentence according to 
the rules described.
"""

def shorten_word(word): 
    if len(word) >= 10: 
        return word[0] + str(len(word)-2) + word[-1] 
    return word

def shorten_sentence (sentence):
    words = sentence.split() 
    return ' '.join([shorten_word(word) for word in words])

# Test case

sentence = "The demonstration of governments laws makes it difficults to understand"
print(shorten_sentence (sentence)) # Output: "the d11n of g9s laws makes it d8s to u8d"

"""def shorten_word(word):
    if len(word) >= 10:
        return f"{word[0]}{len(word) - 2}{word[-1]}"
    return word

def shorten_sentence(sentence):
    words = sentence.split()
    shortened_words = [shorten_word(word) for word in words]
    return ' '.join(shortened_words)

# Example usage:
sentence ="The demonstration of governments laws makes it difficults to understand"
print(shorten_sentence(sentence))  # Output: "the d11n of g9s laws makes it d8s to u8d" 
"""