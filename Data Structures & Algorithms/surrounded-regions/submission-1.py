class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # track safe cells
        m, n = len(board), len(board[0])
        safe = set()
        q = collections.deque()

        for x in range(m):
            if board[x][0] == 'O':
                q.append((x, 0))
            if board[x][n - 1] == 'O':
                q.append((x, n - 1))
        for y in range(n):
            if board[0][y] == 'O':
                q.append((0, y))
            if board[m - 1][y] == 'O':
                q.append((m - 1, y))
        # bfs 
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                safe.add((x, y))

                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny] == 'O' and (nx, ny) not in safe:
                        q.append((nx, ny))
        # if not safe cell -> set to X
        for x in range(m):
            for y in range(n):
                if (x, y) not in safe:
                    board[x][y] = 'X'

