"""
7) 2D Matrix  if k th column is equal to 1 and k th row is equal to 0 
except k-row and k -column it is equal to 0.

return 1 if satisfied otherwise return -1

k=3

[1,1,1]
[1,0,1],
[0,0,0]

Output : 1
"""

def check_matrix(matrix, k):
    n = len(matrix)  # Assuming it's a square matrix (n x n)
    # Check the k-th column (except k-th row)
    for i in range(n):
        if i != k and matrix[i][k] != 1:
            return -1

    # Check the k-th row (except k-th column)
    for j in range(n):
        if j != k and matrix[k][j] != 0:
            return -1
        
    # Check k-th element in k-th row
    if matrix[k][k] != 0:
        return -1

    # If both conditions are satisfied, return 1
    return 1

# Test case
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [0, 0, 0]
]

k = 2# Python uses 0-based indexing, so k = 3 in problem means k = 2 in code
print(check_matrix(matrix, k))  # Output: 1