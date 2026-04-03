class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)

        [38]

        for i, x in enumerate(temperatures):
            while s and temperatures[s[-1]] < x:
                idx = s.pop()
                res[idx] = i - idx
            s.append(i)
        return res
