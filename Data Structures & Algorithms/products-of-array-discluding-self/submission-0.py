class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroIdx = -1
        product = 1

        for i, x in enumerate(nums):
            if x == 0:
                if zeroIdx != -1:
                    res = [0 for x in nums]
                    return res
                else:
                    print("Zero on idx", i)
                    zeroIdx = i
            else:
                product *= x
        
        if zeroIdx != -1:
            res = [0 for x in nums]
            res[zeroIdx] = product
            return res

        for i in range(len(nums)):
            nums[i] = int(product / nums[i])
        
        return nums