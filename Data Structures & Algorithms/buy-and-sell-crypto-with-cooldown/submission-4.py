class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        one = [prices[-1], 0]
        two = [0, 0]

        for i in range(len(prices) - 2, -1, -1):
            temp = [
                max(prices[i] + two[1], one[0]),
                max(0, -prices[i] + one[0], one[1])
            ]

            one, two = temp, one
        return one[1]
        
