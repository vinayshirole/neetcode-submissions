class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = {}

        if len(nums) == len(set(nums)):
            return False
        else:
            return True
            
        for num in nums:
            if num in output:
                return True
            else:
                output[num] = 1

        return False        