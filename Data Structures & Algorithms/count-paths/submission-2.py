class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                grid[r][c] = (grid[r - 1][c] if r > 0 else 0) + (grid[r][c-1] if c > 0 else 0)
        return grid[-1][-1]
