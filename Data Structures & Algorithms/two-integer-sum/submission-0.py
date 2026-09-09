class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen_numbers = {}

        for key, value in enumerate(nums):
            complement = target - value
            if complement not in seen_numbers:
                seen_numbers[value] = key
            else:
                return [seen_numbers[complement], key]