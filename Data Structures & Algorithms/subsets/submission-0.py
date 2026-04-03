class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        seen = {}
        res = []

        def recurse(num):
            if tuple(num) in seen:
                return
            seen[tuple(num)] = True
            res.append(num)
            for i in range(len(num)):
                newNums = num[0:i] + num[i+1:]
                recurse(newNums)
        
        recurse(nums)
        return res
