class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * len(nums)

        memo[-1] = 1
        for i in range(n - 1, -1, -1):
            nMax = 0
            for j in range(i + 1, n):
                if nums[j] <= nums[i]:
                    continue
                nMax = max(nMax, memo[j])
            memo[i] = 1 + nMax
        
        return max(memo)