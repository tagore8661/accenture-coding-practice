"""
Rock, Paper, Scissors -

Two players A and B, are playing the game of Rock, Paper, Scissors. 
Player A chooses a move represented by a string value M and the move can be one of the 
following: 'rock, 'paper', or 'scissors' where.
  
   • rock beats scissors
   • scissors beats paper
   • paper beats rock

Your task is to find and return a string value representing the winning move for Player B.

Note: The output is case sensitive

Input Specification:

Input1: A string value M representing the move chosen by Player A.

Examples :

# Case 1: Player A chooses rock
M = 'rock'
result = winning_move_for_player_B(M)
print(result)  # Output: paper

# Case 2: Player A chooses scissors
M = 'scissors'
result = winning_move_for_player_B(M)
print(result)  # Output: rock

# Case 3: Player A chooses paper
M = 'paper'
result = winning_move_for_player_B(M)
print(result)  # Output: scissors

# Case 4: Invalid move
M = 'lizard'
result = winning_move_for_player_B(M)
print(result)  # Output: Invalid move by Player A


"""

def winning_move_for_player_B(M):
    # Define the winning moves against Player A's move
    if M == 'rock':
        return 'paper'  # Paper beats rock
    elif M == 'scissors':
        return 'rock'  # Rock beats scissors
    elif M == 'paper':
        return 'scissors'  # Scissors beats paper
    else:
        return 'Invalid move by Player A'  # Handle invalid input


# Example usage:
M = input("Enter Player A's move (rock, paper, or scissors): ")
result = winning_move_for_player_B(M)
print(f"Player B's winning move is: {result}")