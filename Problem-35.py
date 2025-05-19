#YT_Techie CodeBuddy

"""Problem Statement:  

It is Edward's birthday today. His friends have bought him a huge circular cake.

Edward wants to find out the maximum number of pieces he can get by making exactly N straight vertical

cuts on the cake. Your task is to write a function that returns the maximum number of pieces that can be obtained by making N number of cuts.

Note: Since the answer can be quite large, modulo it by 1000000007

Input: N = 3
Output: 7

Input: N = 4
Output: 11
"""

def max_pieces(N):
    MOD = 1000000007
    # Using the formula for the Lazy Caterer's Problem
    return (N * (N + 1) // 2 + 1) % MOD

# Example usage
N = 4
print(max_pieces(N))  # Output will be the maximum number of pieces modulo 1000000007


#Another Way

"""def main():
    import sys
    input = sys.stdin.read
    MOD = 1000000007

    n = int(input().strip())
    sum_n = (n * (n + 1)) // 2
    ans = sum_n + 1

    print(ans % MOD)

if __name__ =="__main__":
    main() """