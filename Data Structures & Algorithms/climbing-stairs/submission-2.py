class Solution:
    def climbStairs(self, n: int) -> int:
        steps = {
            0 : 1,
            1 : 1
        }

        def recurse(i):
            if i in steps:
                return steps[i]
            st = recurse(i - 1) + recurse(i - 2)
            steps[i] = st
            return st

        return recurse(n)
