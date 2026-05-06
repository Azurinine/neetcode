class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        q = deque()
        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
        
        res = []
        for l in range(len(nums) - k + 1):
            r = l + k - 1
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)
            
            res.append(nums[q[0]])
            if l == q[0]:
                q.popleft()
        
        return res