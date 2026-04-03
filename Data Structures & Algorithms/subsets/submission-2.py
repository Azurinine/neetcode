class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        st = []
        def dfs(i):
            if i == len(nums):
                res.append(st[:])
                return
            
            # include current index
            st.append(nums[i])
            dfs(i + 1)
            st.pop()

            # exclude current index
            dfs(i + 1)
        dfs(0)
        return res
            
