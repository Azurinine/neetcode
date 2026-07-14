class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        
        arr = [False] * (s // 2 + 1)
        arr[0] = True

        for num in nums:
            for i in range(s // 2, -1, -1):
                if i - num >= 0 and arr[i - num]:
                    arr[i] = True            
            if arr[s // 2]:
                return True
        return False 