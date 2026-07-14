class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float("inf")] * (amount + 1)
        arr[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    arr[i] = min(arr[i-coin] + 1, arr[i])
        
        return -1 if arr[-1] == float("inf") else arr[-1]
