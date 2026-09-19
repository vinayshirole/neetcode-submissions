class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n == 1:
            return 1
        
        left = 0
        seen = set()
        count = 0

        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            count = max(count, right - left + 1)
            seen.add(s[right])
        
        return count