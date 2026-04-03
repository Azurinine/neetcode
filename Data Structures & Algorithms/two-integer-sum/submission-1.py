class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in complement:
                return [complement[diff], i]
            
            complement[n] = i
        