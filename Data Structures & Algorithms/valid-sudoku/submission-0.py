class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        for r in range(len(board)):
            rchecker = dict()
            for c in range(len(board[0])):
                if board[r][c].isdigit():
                    rchecker[board[r][c]] = rchecker.get(board[r][c], 0) + 1
                    if rchecker[board[r][c]] > 1:
                        return False

        for c in range(len(board[0])):
            cchecker = dict()
            for r in range(len(board)):
                if board[r][c].isdigit():
                    cchecker[board[r][c]] = cchecker.get(board[r][c],0) + 1
                    if cchecker[board[r][c]] > 1:
                        return False
            
        for square in range(9):
             bchecker = dict()
             for r in range(3):
                for c in range(3):
                    row = (square//3)*3 + r
                    col = (square%3)*3+c

                    if board[row][col].isdigit():
                        bchecker[board[row][col]] = bchecker.get(board[row][col], 0) + 1
                        if bchecker[board[row][col]] > 1:
                                return False
        
        return True

    
