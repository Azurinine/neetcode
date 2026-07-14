class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        arr = [[0] * (n + 1) for _ in range(2)]

        arr[0][n - 1] = prices[n - 1]
        for i in range(n - 2, -1, -1):
            arr[0][i] = max(prices[i] + arr[1][i + 2], arr[0][i + 1])
            arr[1][i] = max(0, -prices[i] + arr[0][i + 1], arr[1][i + 1])

        return arr[1][0]