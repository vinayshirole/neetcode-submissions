class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if target > matrix[i][n - 1]:
                continue
            
            low = 0
            high = n - 1

            while low <= high:
                mid = (low + high) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            
        return False
