class Solution:
    from collections import Counter

    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        ct = Counter(t)
        l, r = None, None
        found = 0
        res = ""
        for i, ch in enumerate(s):
            if ch in ct:
                if l == None:
                    l = i
                ct[ch] -= 1
                if ct[ch] >= 0:
                    found += 1
                if found == n:
                    r = i
                    res = s[l:r + 1]
                    break
        if found < n:
            return res
        
        while r < len(s):
            if ct[s[l]] < 0:
                ct[s[l]] += 1
                l += 1
                while s[l] not in ct:
                    l += 1
                if r - l < len(res):
                    res = s[l:r + 1]
            else:
                r += 1
                if r < len(s) and s[r] in ct:
                    ct[s[r]] -= 1
        
        return res
