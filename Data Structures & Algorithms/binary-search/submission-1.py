class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        u = len(nums) - 1

        if nums[l] == target:
            return l
        elif nums[u] == target:
            return u

        while (l != u):
            idx = round((l + u) / 2)
            curr = nums[idx]

            if curr == target:
                return idx
            elif curr < target:
                if l == idx:
                    return -1
                l = idx
            else:
                if u == idx:
                    return -1
                u = idx
        
        return u if nums[u] == target else -1