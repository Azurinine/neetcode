class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l,r)]

            cMax = 0
            for i in range(l, r + 1):
                trial = nums[l-1] * nums[i] * nums[r+1] + dfs(l, i - 1) + dfs(i + 1, r)
                cMax = max(trial, cMax)
            
            dp[(l, r)] = cMax
            return cMax
        
        return dfs(1, n)
