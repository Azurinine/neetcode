class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i, j = 0, 0
        
        for k in range(len(prices)):
            if prices[k] > prices[j]:
                j = k
                res = max(res, prices[k] - prices[i])
            elif prices[k] < prices[i]:
                i = j = k
        
        return res
            