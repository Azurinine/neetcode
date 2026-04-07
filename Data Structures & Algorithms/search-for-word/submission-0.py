class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        checked = {}
        r = len(board)
        c = len(board[0])

        def dfs(x, y, i):
            nonlocal checked
            if i == len(word):
                return True

            adjSq = self.adj(x, y, word[i], board)
            found = False
            for sq in adjSq:
                if sq not in checked and not found:
                    checked[sq] = True
                    found = dfs(*sq, i + 1)
                    del checked[sq]
            return found

        for x in range(r):
            for y in range(c):
                if board[x][y] == word[0]:
                    checked[(x, y)] = True
                    if dfs(x, y, 1):
                        return True
                    del checked[(x,y)]
        return False



    def adj(self, x, y, ch, board):
        res = []
        cAdd = [(0, 1), (1, 0), (0,-1),(-1,0)]
        r = len(board)
        c = len(board[0])
        for xAdd, yAdd in cAdd:
            xNew = x + xAdd
            yNew = y + yAdd
            if 0 <= xNew < r and 0 <= yNew < c and board[xNew][yNew] == ch:
                res.append((xNew, yNew)) 
        return res
        

                    