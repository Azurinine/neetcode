class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [-1] * (amount + 1)
        arr[0] = 0
        for i in range(1, amount + 1):
            cMin = float("inf")
            for coin in coins:
                if i - coin >= 0:
                    cMin = min(arr[i-coin] + 1, cMin)
                arr[i] = cMin 
        
        return -1 if arr[-1] == float("inf") else arr[-1]
