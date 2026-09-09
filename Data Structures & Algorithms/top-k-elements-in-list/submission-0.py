class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        values = []
        for num in nums:
            if num in output:
                output[num] += 1
            else:
                output[num] = 1
        output = dict(sorted(output.items(), key=lambda x:x[1], reverse=True))

        for key, value in output.items():
            if k != 0:
                values.append(key)
                k -= 1
        
        return values
