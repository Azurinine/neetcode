class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # ABBABBA -> ABBABBA, ABBA:ABBA, A:BB:AA:BB:A, A:BB:A:A:BB:A, A:B:B:A:A:B:B:A
        # A:BBA
        # st = [1,4]
        st = [0]
        res = []

        def check(i):
            l, r = st[-1], i - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if i == len(s):
                if check(i):
                    st.append(i)
                    res.append(["".join(s[st[i]:st[i+1]]) for i in range(0, len(st) - 1)])
                    st.pop()
                return
            
            if check(i):
                st.append(i)
                dfs(i + 1)
                st.pop()
            
            dfs(i + 1)
        
        dfs(1)
        return res
                        