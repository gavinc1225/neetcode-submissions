class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        l, r = 0, 1
        curr_profit = 0
        while r < len(prices):
            curr_profit = max(curr_profit, prices[r] - prices[l])
            if prices[l] >= prices[r]:
                l = r
            
            r += 1
        
        return curr_profit
            
