class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, check):
            cSum = sum(curr)
            if check and cSum == target:
                res.append(curr.copy())
            if cSum >= target or i >= len(nums):
                return
            
            curr.append(nums[i])
            dfs(i, True)

            curr.pop()
            dfs(i + 1, False)

        dfs(0, False)
        return res