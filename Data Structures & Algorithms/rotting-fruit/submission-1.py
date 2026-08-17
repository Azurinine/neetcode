class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # track number of fresh fruits
        m, n = len(grid), len(grid[0])

        q = collections.deque()
        fresh_num = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    fresh_num += 1
                elif grid[x][y] == 2:
                    q.append((x,y)) # initalize queue with rotten oranges
        if not fresh_num:
            return 0
        # bfs; keep track of layer
        time = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_num -= 1
                        q.append((nx, ny))
            time += 1

        # if no fresh fruits return
        return -1 if fresh_num else time - 1