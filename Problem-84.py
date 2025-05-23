"""find the rhymeWords 
Input : S = "thunder"
        D = ["pukle", "thunder", "powder", "blender", "under"]

output : under
"""

def rhymeWords(S, D):
    best_word = "No Word"
    max_match_length = 0
    
    for word in D:
        if word == S:
            continue
        
        # Find the longest matching suffix
        min_length = min(len(S), len(word))
        match_length = 0
        
        for i in range(1, min_length + 1):
            if S[-i] == word[-i]:
                match_length += 1
            else:
                break
        
        # Update best_word if this word has a longer matching suffix
        if match_length > max_match_length:
            max_match_length = match_length
            best_word = word
    
    return best_word
            
            
def main():
    S = "thunder"
    D = ["pukle", "thunder", "powder", "blender", "under"]
    output = rhymeWords(S, D)
    print(output) 
    

if __name__ == "__main__":
    main()


"""
def find_rhyme_word(S, D):
    def get_suffix(word):
        # Get the last two characters of the word
        return word[-2:]

    target_suffix = get_suffix(S)
    for word in D:
        if word != S and get_suffix(word) == target_suffix:
            return word

# Sample Test Case
S = "thunder"
D = ["pukle", "thunder", "powder", "blender", "under"]

print(find_rhyme_word(S, D))  # Output: under

"""