class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev = [0] * (len(t) + 1)
        curr = [0] * (len(t) + 1)
        prev[-1] = curr[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t)):
                curr[j] = prev[j]
                if s[i] == t[j]:
                    curr[j] += prev[j + 1]
            prev, curr = curr, prev
        return prev[0]