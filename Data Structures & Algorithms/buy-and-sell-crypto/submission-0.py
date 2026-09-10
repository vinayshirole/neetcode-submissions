class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1

        max_profit = 0

        while right < len(prices):

            if prices[right] < prices[left]:
                left = right
                right = left + 1
            else:
                profit = prices[right] - prices[left]
                right += 1
            
                max_profit = max(profit, max_profit)
        
        return max_profit