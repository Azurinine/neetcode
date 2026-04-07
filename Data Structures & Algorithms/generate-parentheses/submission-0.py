class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st = []
        res = []

        def dfs(ct1):
            if len(st) == 2*n:
                res.append("".join(st))
                return
            
            if ct1 < n:
                st.append("(")
                dfs(ct1 + 1)
                st.pop()
            if len(st) - ct1 < ct1:
                st.append(")")
                dfs(ct1)
                st.pop()
        
        dfs(0)
        return res

        # st = ["((()))"]