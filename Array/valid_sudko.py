from collections import defaultdict


def isValidSudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    square = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if(board[r][c] == '.'):
                continue
            if(board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in square[r//3, c//3]):
                return False
            
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            square[r//3,c//3].add(board[r][c])

    return True

board = [[".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
print(isValidSudoku(board)) 