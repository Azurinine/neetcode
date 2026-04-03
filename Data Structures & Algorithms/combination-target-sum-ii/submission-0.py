class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        cand = sorted(candidates)
        def recurse(i):
            cSum = sum(stack)
            if i >= len(cand) or cSum >= target:
                if cSum == target:
                    res.append(stack.copy())
                return

            cNum = cand[i]
            j = 1
            while j + i < len(cand) and cand[i + j] == cNum:
                j += 1
                
            for _ in range(j):
                stack.append(cNum)
                recurse(i + j)
            
            for _ in range(j):
                stack.pop()
            recurse(i + j)
        
        recurse(0)
        return res
        # [1, 2, 2]
        #                    []
        #         [1]                      []
        # [1]  [1, 2] [1, 2, 2]      [2] [2, 2] []