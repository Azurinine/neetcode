class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = []
        rightProd = []

        runLeft = 1
        runRight = 1

        length = len(nums)
        
        for i in range(length):
            runLeft *= nums[i]
            runRight *= nums[length - 1 - i]

            leftProd.append(runLeft)
            rightProd.append(runRight)

        rightProd.reverse()

        res = [rightProd[1]]

        for i in range(1, length - 1):
            res.append(leftProd[i - 1] * rightProd[i + 1])
        
        res.append(leftProd[length - 2])
        print(leftProd, rightProd)

        return res