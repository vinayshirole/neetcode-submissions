class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            sum = 0
            while n != 0:
                digit = n % 10
                n = n // 10
                sum += digit ** 2
            
            if sum == 1:
                return True
            elif sum in seen:
                return False
            else:
                n = sum
                seen.add(sum)
