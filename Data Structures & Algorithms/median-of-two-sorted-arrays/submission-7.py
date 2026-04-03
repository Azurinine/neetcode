class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums2) < len(nums1):
            A, B = B, A
        
        size = len(A) + len(B)
        median = size // 2
        l, r = 0, len(A) - 1
        while True:
            a = (l + r) // 2
            b = median - a - 2

            a_l = A[a] if a >= 0 else float("-inf")
            b_l = B[b] if b >= 0 else float("-inf")
            a_r = A[a + 1] if a + 1 < len(A) else float('inf')
            b_r = B[b + 1] if b + 1 < len(B) else float('inf')

            if a_l <= b_r and b_l <= a_r:
                if size % 2:
                    return min(a_r, b_r)
                return (max(a_l, b_l) + min(a_r, b_r)) / 2
            if a_l > b_r:
                r = a - 1
            else:
                l = a + 1

            