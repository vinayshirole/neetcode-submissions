class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            grid[i][0] = i

        for j in range(n + 1):
            grid[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    grid[i][j] = grid[i - 1][j - 1]
                else:
                    grid[i][j] = 1 + min(grid[i][j - 1], grid[i - 1][j], grid[i - 1][j - 1])
        
        return grid[-1][-1]

# [

#     ""  m  o  n  k  e  y  s
# ""  [0, 1, 2, 3, 4, 5, 6, 7], 
# m   [1, 0, 1, 2, 3, 4, 5, 6], 
# o   [2, 1, 0, 1, 2, 3, 4, 5], 
# n   [3, 2, 1, 0, 1, 2, 3, 4], 
# e   [4, 3, 2, 1, 1, 1, 2, 3], 
# y   [5, 4, 3, 2, 2, 2, 1, 2]

# ]