class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = nums[0]
        one, two = 0, 0

        nums[0] = 0
        for num in nums:
            temp = num + two
            two = max(two, one)
            one = temp
        res1 = max(one, two)
        
        nums[0] = l
        nums[-1] = 0
        one, two = 0, 0
        for num in nums:
            temp = num + two
            two = max(two, one)
            one = temp

        return max(res1, one, two)




