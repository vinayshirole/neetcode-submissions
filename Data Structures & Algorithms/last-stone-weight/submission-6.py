class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_weight = max(stones)
        buckets = [0] * (max_weight + 1)
        
        # Populate frequency array
        for stone in stones:
            buckets[stone] += 1
            
        first = max_weight
        second = max_weight
        
        while first > 0:
            # Find the largest weight available
            while first > 0 and buckets[first] == 0:
                first -= 1
            if first == 0:
                break
            
            # If an even number of stones of weight 'first' exist, they cancel each other out
            buckets[first] %= 2
            
            # If 1 stone remains, find the next largest stone to smash it with
            if buckets[first] == 1:
                second = first - 1
                while second > 0 and buckets[second] == 0:
                    second -= 1
                
                # If no second stone exists, 'first' is the last remaining stone
                if second == 0:
                    return first
                
                # Smash 'first' and 'second'
                buckets[first] -= 1
                buckets[second] -= 1
                buckets[first - second] += 1
                
                # Reset search pointer to the top remaining potential weight
                first = max(first - second, second)
                
        return 0