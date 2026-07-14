class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        
        ROWS, COLS = len(nums), s // 2
        
        dp = [[False] * (COLS + 1) for _ in range(ROWS)]
        for r in range(ROWS):
            dp[r][0] = True

        for c in range(1, COLS + 1):
            for r in range(ROWS):
                cond1 = r > 0 and dp[r-1][c]
                cond2 = r > 0 and c - nums[r] >= 0 and dp[r-1][c-nums[r]]
                dp[r][c] = cond1 or cond2 or nums[r] == c
        
        return dp[ROWS - 1][COLS]

            


        
