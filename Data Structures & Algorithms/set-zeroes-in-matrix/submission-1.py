class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, columns = len(matrix), len(matrix[0])
        row_flag, col_flag = False, False
        for row in range(rows):
            for col in range(columns):
                if matrix[row][col] == 0:
                    if row == 0:
                        row_flag = True
                    if col == 0:
                        col_flag = True
                    if row != 0 and col != 0:
                        matrix[row][0] = 0
                        matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, columns):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if row_flag:
            matrix[0] = [0] * columns
        
        if col_flag:
            for i in range(rows):
                matrix[i][0] = 0