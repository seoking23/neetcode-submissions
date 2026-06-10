class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1
        while l < len(prices) - 1:         
            if prices[r] > prices[l]:
                maxProfit = max(prices[r] - prices[l], maxProfit)
            else:
                l = r
            if r < len(prices) - 1:
                r += 1
            else:
                l += 1
        
        
        return maxProfit
                