class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        r, c = len(grid), len(grid[0])

        cardinal = ((0,1),(1,0),(-1,0),(0,-1))
        def dfs(x, y):
            if not 0 <= x < r or not 0 <= y < c or not grid[x][y]:
                return 0
            
            area = 1
            grid[x][y] = 0
            for i, j in cardinal:
                area += dfs(x + i, y + j)
            
            return area
        
        for x in range(r):
            for y in range(c):
                if grid[x][y]:
                    res = max(res, dfs(x, y))
        
        return res