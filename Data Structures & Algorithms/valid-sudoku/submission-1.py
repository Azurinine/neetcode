class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [0] * 9
            col = [0] * 9
            for j in range(9):
                if board[i][j] != ".":
                    row_num = int(board[i][j]) - 1
                    if row[row_num]:
                        return False
                    row[row_num] = 1

                if board[j][i] != ".":
                    col_num = int(board[j][i]) - 1
                    if col[col_num]:
                        return False
                    col[col_num] = 1
        
        for i in range(3):
            start_row = i * 3
            end_row = start_row + 3
            for j in range(3):
                start_col = j * 3
                end_col = start_col + 3
                sq = [0] * 9
                for r in range(start_row, end_row):
                    for c in range(start_col, end_col):
                        if board[r][c] != ".":
                            sq_num = int(board[r][c]) - 1
                            if sq[sq_num]:
                                return False
                            sq[sq_num] = 1
        return True





