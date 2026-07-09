class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])

        cardinal = ((-1, 0), (0, -1), (1, 0), (0, 1))
        def dfs(x, y):
            if (not 0 <= x < m) or (not 0 <= y < n) or grid[x][y] == "0":
                return

            grid[x][y] = "0"
            for i, j in cardinal:
                dfs(x + i, y + j)
                
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    res += 1
                    dfs(x,y)
        
        return res