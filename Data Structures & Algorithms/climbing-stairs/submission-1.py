class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        output = [0] * n
        output[0] = 1
        output[1] = 2
        for i in range(2, n):
            output[i] = output[i - 2] + output[i - 1]
        
        return output[-1]
