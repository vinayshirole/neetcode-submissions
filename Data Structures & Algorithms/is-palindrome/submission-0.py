class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = ""
        for ch in s:
            if ch.isalnum():
                output += output.join(ch.lower())

        left = 0
        right = len(output) - 1

        while left <= right:
            if output[left] != output[right]:
                return False
            left += 1
            right -= 1
        
        return True