class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        max_time = 0

        if len(piles) == h:
            return high
        
        while low <= high:
            mid = (low + high) // 2
            time = 0
            for banana in piles:
                if banana <= mid:
                    time += 1
                else:
                    time += (banana // mid)
                    if banana % mid != 0:
                        time += 1

            if time <= h:
                res = mid  
                high = mid - 1
            else:
                low = mid + 1  
                
        return res