class Solution:
    def rob(self, nums: List[int]) -> int:

        one, two, three = 0, 0, 0
        for i in range(len(nums) - 1, -1, -1):
            one, two, three = nums[i] + max(two, three), one, two

        return max(one, two)