class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pNew = []
        i = 0
        while i < len(p):
            if i != len(p) - 1 and p[i + 1] == "*":
                pNew.append(p[i] + "*")
                i += 2
            else:
                pNew.append(p[i])
                i += 1
        p = pNew
        m, n = len(s), len(p)
        prev = [False] * (m + 1)
        curr = [False] * (m + 1)
        prev[m] = True

        print(prev)

        for i in range(n - 1, -1, -1):
            if len(p[i]) == 2:
                curr[m] = prev[m]
            for j in range(m - 1, -1, -1):
                if len(p[i]) == 2:
                    if p[i][0] == ".":
                        curr[j] = curr[j + 1] or prev[j + 1] or prev[j]
                    elif p[i][0] != s[j]:
                        curr[j] = prev[j]
                    else:
                        case1 = prev[j + 1] or prev[j]
                        case2 = j + 1 < m and curr[j + 1] and s[j + 1] == s[j]
                        curr[j] = case1 or case2
                else:
                    curr[j] = prev[j + 1] and (p[i] == "." or p[i] == s[j])
            prev = curr.copy()
            
            print(prev)
        
        return prev[0]