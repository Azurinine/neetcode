class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # [2,9,8,3,6]
        # [16,15,14,3,6]

        one, two = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            cCost = nums[i] + two
            one, two = cCost, max(one, two)

        return max(one, two)