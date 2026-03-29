class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = profit = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            profit = -prices[l] + prices[r]
            best = max(profit, best)
        return best

            
            