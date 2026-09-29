class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        row = 0
        min_rows, max_rows = 0, len(matrix)
        min_cols, max_cols = 0, len(matrix[0])

        while min_rows < max_rows and min_cols < max_cols:
            for col in range(min_cols, max_cols):
                output.append(matrix[row][col])
            min_rows += 1

            for row in range(min_rows, max_rows):
                output.append(matrix[row][col])
            max_cols -= 1

            if min_rows < max_rows and min_cols < max_cols:
                for col in range(max_cols - 1, min_cols - 1, -1):
                    output.append(matrix[row][col])
                max_rows -= 1

                for row in range(max_rows - 1, min_rows - 1, -1):
                    output.append(matrix[row][col])
                min_cols += 1
        
        return output