class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        checked = {}

        for idx, x in enumerate(nums):
            if (x > 0):
                break
            if x in checked:
                continue
            else:
                checked[x] = 0
            
            # Require -x
            i, j = idx + 1, len(nums) - 1
            while (i < j):
                total = nums[i] + nums[j]
                if (total == -x):
                    res.append([x, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while (i < j):
                        if (nums[i] == nums[i - 1]):
                            i += 1
                        else:
                            break
                elif (total < -x):
                    i += 1
                else: 
                    j -= 1

        return res

                