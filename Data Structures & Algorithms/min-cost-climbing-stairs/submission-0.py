class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [ 1 2 3 ]
        # [ 3 2 3 0 ]

        one, two = 0, 0
        for i in range(len(cost) - 1, -1, -1):
            cCost = cost[i] + min(one, two)
            one, two = cCost, one

        return min(one, two)