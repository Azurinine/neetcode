class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        arr = [0] * (n + 2)
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if (prices[j] > prices[i]):
                    arr[i] = max(arr[i], prices[j] - prices[i] + arr[j + 2])
                else:
                    arr[i] = max(arr[i], arr[j])
        return max(arr)