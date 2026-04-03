class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        res = 0

        while (i < j):
            left, right = heights[i], heights[j]
            if (left < right):
                res = max(res, left * (j - i))
                i += 1
            else:
                res = max(res, right * (j - i))
                j -= 1 
        return res