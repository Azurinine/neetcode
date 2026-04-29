class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res, resLen = 0, 1

        def checkLen(l, r):
            nonlocal res, resLen
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > resLen:
                res = l + 1
                resLen = r - l - 1

        for i in range(1, n):
            checkLen(i, i)
            checkLen(i - 1, i)

        return s[res : res + resLen]

        