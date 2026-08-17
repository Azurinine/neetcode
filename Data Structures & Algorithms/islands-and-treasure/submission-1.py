class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        
        # insert all 0's into queue 
        q = collections.deque()
        for x in range(m):
            for y in range(n):
                if not grid[x][y]:
                    q.append((x,y))

        # bfs
        dist = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()     
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if grid[nx][ny] > dist + 1:
                        grid[nx][ny] = dist + 1
                        q.append((nx, ny))
            dist += 1




        
        

        
