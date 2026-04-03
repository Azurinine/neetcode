class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        MAX = max(piles)
        if len(piles) == h:
            return MAX

        l, r = 1, MAX
        res = MAX

        while (l <= r):
            rate = (l + r) // 2
            total = 0
            for x in piles:
                total += math.ceil(x / rate)

            if total > h:
                l = rate + 1
            else:
                r = rate - 1
                res = min(rate, MAX)
        
        return res




