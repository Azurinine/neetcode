class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            
            if nums[l] < nums[m]:
                if nums[l] < target and target < nums[m]:
                    r = m - 1
                else: 
                    l = m + 1
            else:
                if target < nums[l] and target < nums[m]:
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
