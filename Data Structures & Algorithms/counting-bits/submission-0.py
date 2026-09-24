class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            ct = 0
            while num:
                if num & 1: ct += 1
                num >>= 1
            res.append(ct)
        return res