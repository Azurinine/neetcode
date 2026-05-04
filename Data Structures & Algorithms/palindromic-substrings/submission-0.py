class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def check(i):
            nonlocal count
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            check(i)
        
        return count