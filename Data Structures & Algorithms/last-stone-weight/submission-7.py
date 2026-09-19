import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
            
        heapq.heapify(stones)

        while len(stones) > 1:
            diff = heapq.heappop(stones) - heapq.heappop(stones)
            if diff:
                heapq.heappush(stones, diff)

        return -stones[0] if stones else 0