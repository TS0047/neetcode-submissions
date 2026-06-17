class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            row = []
            col = []
            for j in range(0,9):
                if board[i][j] != ".":
                    row.append(board[i][j])
                if board[j][i] != ".":
                    col.append(board[j][i])
            if (len(set(row)) != len(row)) or (len(set(col)) != len(col)):
                return False

        for i in range(0,3):
            for j in range(0,3):
                grid = []
                for k in range(i*3,i*3+3):
                    for l in range(j*3,j*3+3):
                        if board[k][l]!=".":
                            grid.append(board[k][l])
                if len(set(grid)) != len(grid):
                    return False
        return True

