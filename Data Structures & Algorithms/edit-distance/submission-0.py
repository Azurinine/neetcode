class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m > n:
            m, n = n, m
            word1, word2 = word2, word1
        
        # m < n, word1 < word2
        dp = [0] * (m + 1)
        nextDp = [0] * (m + 1)

        for i in range(m + 1):
            dp[i] = m - i
        
        for i in range(n - 1, -1, -1):
            nextDp[m] = n - i
            for j in range(m - 1, -1, -1):
                nextDp[j] = min(dp[j + 1], dp[j], nextDp[j + 1]) + 1
                if word2[i] == word1[j]:
                    nextDp[j] = min(nextDp[j], dp[j + 1])
            dp = nextDp[:]
        
        return dp[0]
