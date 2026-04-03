class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = nums[0]

        n = len(nums)
        lo, hi = 0, n - 1
        while (lo <= hi):
            m = (lo + hi) // 2
            if (m == n - 1):
                return first if first < nums[m] else nums[m]
            if (m == 0):
                return first if first < nums[m + 1] else nums[m + 1]

            if nums[m + 1] < nums[m]:
                return nums[m + 1]
            if nums[m - 1] > nums[m]:
                return nums[m]
            elif nums[m - 1] > nums[m]:
                return nums[m + 1]
            elif nums[m] > first: # In rotated section
                lo = m + 1
            else:
                hi = m - 1
    
        return first
        