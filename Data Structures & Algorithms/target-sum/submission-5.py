class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, cSum):
            if i == len(nums):
                return 1 if cSum == target else 0
            return dfs(i + 1, cSum + nums[i]) + dfs(i + 1, cSum - nums[i])
        
        return dfs(0, 0)
