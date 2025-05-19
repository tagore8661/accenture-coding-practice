"""You are playing a game of Toss and Score in the Hillwood City Mall with your friends. The game consists of the following rules:

• Toss an unbiased coin multiple times.

• For each heads you get 2 points and for each tails you lose 1 point.

• The game ends as soon as you get 3 heads in a row, or you toss the coin throughtout the length of string S.

You have been given a string S consisting of letters H (for heads) and T (for tails) denoting the sequence results you get on the toss of coin N times. 
Your task is to find and return an integer value, representing the final score you get once the game ends."""

def toss_and_score(str):
    count = 0
    count_head = 0
    for i in str:
        if i == 'H':
            count += 2
            count_head +=1
            if count_head == 3:
                break
        else:
            count -= 1
            count_head = 0
    return count

str = input()
print(toss_and_score(str))