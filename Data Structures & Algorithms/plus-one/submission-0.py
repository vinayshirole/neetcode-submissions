class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = 0
        n = len(digits)

        for i in range(n):
            output += (digits[i] * 10 ** (n - i - 1))
        
        output = str(output + 1)

        final = [0] * len(output)

        for i in range(len(output)):
            final[i] = output[i]
        
        return final