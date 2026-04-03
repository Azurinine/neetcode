class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if (s == ""):
            return 0

        res, l = 0, 0
        hashmap = {s[0] : 1}

        for r in range(1, len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            cur = r - l + 1

            if cur - max(hashmap.values()) <= k:
                res = max(res, cur)
            else: 
                hashmap[s[l]] -= 1
                l += 1
        
        return max(res, r - l)