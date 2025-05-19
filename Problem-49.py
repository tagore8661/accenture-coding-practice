"""
5) N th term of a special febonachi series. it will be return the addition of previuse M numbers and return new specisl febonachi series

input : N = 7
        M = 3

Output : 0,1,1,2,4,7,13
"""

def special_fibonacci_series(N, M):
    # Initialize the sequence with the first M terms
    sequence = [0] * (M - 1) + [1] #[0, 0, 1]
    
    # Generate the sequence up to the Nth term
    for i in range(M, N + 1):
        next_term = sum(sequence[-M:])
        sequence.append(next_term)
    
    return sequence

# Example usage:
N = 7
M = 3
print(special_fibonacci_series(N, M))  # Output will be [0, 0, 1, 1, 2, 4, 7,13]