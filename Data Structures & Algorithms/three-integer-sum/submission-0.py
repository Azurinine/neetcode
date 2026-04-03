class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx, x in enumerate(nums):
            # Require -x
            i, j = idx + 1, len(nums) - 1
            while (i < j):
                total = nums[i] + nums[j]
                if (total == -x):
                    new = [x, nums[i], nums[j]]
                    if (new not in res):
                        res.append(new)
                    i += 1
                elif (total < -x):
                    i += 1
                else: 
                    j -= 1

        return res

                