class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [["."] * n for _ in range(n)]
        col = set()
        pos = set()
        neg = set()
        
        def dfs(r):
            nonlocal board, col, pos, neg
            if r == n:
                res.append(["".join(r) for r in board])
                return

            for c in range(n):
                if c in col or c + r in pos or c - r in neg:
                    continue
                col.add(c)
                pos.add(c + r)
                neg.add(c - r)

                board[r][c] = "Q"
                dfs(r + 1)
                board[r][c] = "."

                col.remove(c)
                pos.remove(c + r)
                neg.remove(c - r)
        
        dfs(0)
        return res
