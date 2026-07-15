class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cardinal = ((-1,0),(0,-1),(1,0),(0,1))

        path = [[0] * n for _ in range(m)]
        def dfs(i, j):
            if path[i][j]:
                return path[i][j]
            
            cur = matrix[i][j]
            mLen = 0
            for di, dj in cardinal:
                if 0 <= i + di < m and 0 <= j + dj < n and matrix[i + di][j + dj] > cur:
                    mLen = max(mLen, dfs(i + di, j + dj))

            path[i][j] = mLen + 1
            return mLen + 1
        
        cMax = 1
        for i in range(m):
            for j in range(n):
                cMax = max(cMax, dfs(i, j))
        return cMax
        
