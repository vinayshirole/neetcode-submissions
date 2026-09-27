class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows    = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        grid    = [set() for _ in range(9)]
    
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num != '.':
                    index = (row // 3) * 3 + (column // 3)
                    if num in rows[row] or num in columns[column] or num in grid[index]:
                        return False
                    else:
                        rows[row].add(num)
                        columns[column].add(num)
                        grid[index].add(num)
        
        return True