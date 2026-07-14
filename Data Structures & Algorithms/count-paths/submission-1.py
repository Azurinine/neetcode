class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [1] * n
        for _ in range(m - 1):
            for i in range(n):
                grid[i] = grid[i] + (grid[i - 1] if i > 0 else 0)
        return grid[-1]
