class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        b = 0 
        s = 1
        maxP = 0
        while s < len(prices):
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                maxP = max(maxP, profit)
            
            else:
                b = s


            s += 1
        return maxP