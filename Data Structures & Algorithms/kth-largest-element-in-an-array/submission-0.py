class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)
        for i in range(k, len(nums)):
            if h[0] < nums[i]:
                heapq.heappushpop(h, nums[i])
        
        return h[0]