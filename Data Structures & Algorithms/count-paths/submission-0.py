class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, columns = m, n

        grid = [[0 for j in range(columns)] for i in range(rows)]
        
        for i in range(rows):
            grid[i][0] = 1

        for j in range(columns):
            grid[0][j] = 1
        
        for i in range(1, rows):
            for j in range(1, columns):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        
        return grid[-1][-1]