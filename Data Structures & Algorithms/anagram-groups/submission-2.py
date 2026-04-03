class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict, Counter
        res = defaultdict(list)

        for s in strs:
            key = frozenset(Counter(s).items())
            res[key].append(s)
    
        return list(res.values())

