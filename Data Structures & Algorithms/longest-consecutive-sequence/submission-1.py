class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_len = 0

        for x in nums:
            if x - 1 in nums:
                continue
            length = 1

            while x + length in nums:
                length += 1
            
            max_len = max(max_len, length)
        
        return max_len
            
            