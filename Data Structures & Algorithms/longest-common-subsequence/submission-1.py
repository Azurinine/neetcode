class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                up = dp[r - 1][c] if r > 0 else 0
                left = dp[r][c - 1] if c > 0 else 0
                match = (dp[r - 1][c - 1] if r > 0 and c > 0 else 0) + (1 if text1[r] == text2[c] else 0)
                dp[r][c] = max(up, left, match)
        return dp[-1][-1]
                



            

                