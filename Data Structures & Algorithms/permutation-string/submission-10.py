class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        mapping, current = [0] * 26, [0] * 26

        l, r = 0, len(s1)
        a = ord('a')
        for x in range(r):
            mapping[ord(s1[x]) - a] += 1
            current[ord(s2[x]) - a] += 1
        
        while r < len(s2):
            if (mapping == current):
                return True

            current[ord(s2[l]) - a] -= 1
            current[ord(s2[r]) - a] += 1

            l += 1
            r += 1
        
        return mapping == current



