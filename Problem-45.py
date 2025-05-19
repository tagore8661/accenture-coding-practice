"""
1) Print the winning team of football match, the team with most goals is the winner
Sample input :6

TeamA
TeamA
TeamB
TeamA
TeamB
TeamB

Output : TeamA
"""
def find_winning_team(goals):
    # Create a dictionary to count the goals for each team
    goal_count = {}
    
    # Count the goals for each team
    for team in goals:
        if team in goal_count:
            goal_count[team] += 1
        else:
            goal_count[team] = 1
    
    # Find the team with the maximum goals
    winning_team = max(goal_count, key=goal_count.get)
    return winning_team

# Example usage:
goals = ["TeamA", "TeamA", "TeamB", "TeamA", "TeamB", "TeamB"]
print(find_winning_team(goals))  # Output will be "TeamA"