import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        output = []

        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt(pow(x, 2) + pow(y, 2))
            pair = (distance, [x, y])
            heapq.heappush(heap, pair)
        
        for i in range(k):
            number = heapq.heappop(heap)
            output.append(number[1])
        
        return output