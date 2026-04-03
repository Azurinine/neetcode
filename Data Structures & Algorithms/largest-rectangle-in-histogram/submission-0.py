class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights) - 1
        left = [l + 1- i for i in range(l + 1, 0, -1)]
        right = [l - i for i in range(l + 1)]


        l_st, r_st = [], []
        for i in range(l + 1):
            l_idx = l - i
            while r_st and heights[r_st[-1]] > heights[i]:
                idx = r_st.pop()
                right[idx] = i - idx - 1
            while l_st and heights[l_st[-1]] > heights[l_idx]:
                idx = l_st.pop()
                left[idx] =  idx - l_idx - 1
            r_st.append(i)
            l_st.append(l_idx)
        print(left)
        print(right)

        max_area = 0
        for i in range(l+1):
            max_area = max(heights[i]*(left[i] + right[i] + 1), max_area)
        
        return max_area
    
    # [0 1 2]
    # [1 3 7]
    # l_st = []
    # left = [0 1 2] 
    # []
    # i = 1, l_idx = 5 - i = 4
