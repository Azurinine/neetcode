class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stash = {}
        res = []
        st = []
        def dfs():
            if len(stash) == len(nums):
                res.append(st.copy())
                return
            for x in nums:
                if x not in stash:
                    stash[x] = True
                    st.append(x)
                    dfs()
                    del stash[st.pop()]

        dfs()
        return res

        