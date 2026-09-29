class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(n + 1):
            if i > 1:
                output[i] = output[i & (i - 1)] + 1
            elif i == 0:
                output[i] = 0
            else:
                output[i] = 1
        
        return output