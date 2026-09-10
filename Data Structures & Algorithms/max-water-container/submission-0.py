class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = -1 * float('inf')
        left = 0
        right = len(heights) - 1

        while left != right:
            temp_volume = min(heights[left], heights[right]) * (right - left)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            volume = max(temp_volume, volume)
        
        return volume
        