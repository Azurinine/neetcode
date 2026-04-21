class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digToCh = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        if not digits:
            return []

        res = []
        st = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(st))
                return
            
            for ch in digToCh[int(digits[i]) - 2]:
                st.append(ch)
                dfs(i + 1)
                st.pop()
        
        dfs(0)
        return res
