class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cMax, cMin = 1, 1

        for num in nums:
            temp = cMax * num
            cMax = max(num, temp, num * cMin)
            cMin = min(num, temp, num * cMin)
            res = max(res, cMax)
        
        return res