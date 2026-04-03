class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord('a')] += 1
            res[tuple(key)].append(s)
    
        return list(res.values())

