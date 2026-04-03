class Solution:
    def trap(self, height: List[int]) -> int:
        lSum = [0] * len(height)
        rSum = [0] * len(height)

        lMax, rMax = height[0], height[-1]
        for i in range(len(height)):
            lMax = max(lMax, height[i])
            rMax = max(rMax, height[-i-1])
            lSum[i] = lMax
            rSum[-i-1] = rMax
        
        res = 0
        for i in range(len(height)):
            res += min(lSum[i], rSum[i]) - height[i]

        return res
