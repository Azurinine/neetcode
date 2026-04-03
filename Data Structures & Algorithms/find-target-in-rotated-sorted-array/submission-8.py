class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            mid = nums[m]
            if mid == target:
                return m

            isLeft = True
            if mid < target:
                isLeft = not(target <= nums[r] or nums[r] < mid)
            else:
                isLeft = nums[l] <= target or mid < nums[l]
            
            if isLeft:
                r = m - 1
            else:
                l = m + 1
        
        return -1
        
      
# [L X X M X X X R] t = 7
# [10 0 9 0 0 0]

#  L -> l < t < M or l < 
#  R -> r < t < M

# [X X X 4 X X X X] mid < num
#     [X X X 4 X X X 9] right >= num -> R
#     [6 X X 4 X X X 5] left <= num -> L
#     [9 X X 4 X X X 5]  
