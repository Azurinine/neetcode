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
        print(lSum)
        print(rSum)
        
        res = 0
        for i in range(len(height)):
            h = min(lSum[i], rSum[i])
            if h - height[i] > 0:
                res += h - height[i]

        return res
