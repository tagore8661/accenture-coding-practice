# Question 5: Unique Paths in a Grid
class UniquePaths:
    def __init__(self, grid):
        self.grid = grid

    def find_paths(self):
        rows, cols = len(self.grid), len(self.grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1 if self.grid[0][0] == 0 else 0
        for i in range(rows):
            for j in range(cols):
                if self.grid[i][j] == 0:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]
    
# Example: Unique Paths in a Grid
grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
up = UniquePaths(grid)
print("Unique Paths:", up.find_paths())  # Output: 2