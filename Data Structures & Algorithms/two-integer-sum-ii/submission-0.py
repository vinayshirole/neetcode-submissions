class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = {}

        for key, value in enumerate(numbers):
            key += 1
            complement = target - value
            if complement in output:
                return [output[complement], key]
            output[value] = key
        
        return -1