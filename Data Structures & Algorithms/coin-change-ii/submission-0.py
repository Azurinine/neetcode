class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev = [0] * (amount + 1)
        curr = [0] * (amount + 1)
        prev[0], curr[0] = 1, 1

        for coin in coins:
            for i in range(1, amount + 1):
                curr[i] = prev[i] + (curr[i - coin] if i - coin >= 0 else 0)
            prev, curr = curr, prev
        
        return prev[-1]