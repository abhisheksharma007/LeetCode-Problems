import time
from collections import defaultdict

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

board1 = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

board2 = [[".",".","4",".",".",".","6","3","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,["5",".",".",".",".",".",".","9","."]
        ,[".",".",".","5","6",".",".",".","."]
        ,["4",".","3",".",".",".",".",".","1"]
        ,[".",".",".","7",".",".",".",".","."]
        ,[".",".",".","5",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]]

def sudoku_checker(board):
    rows = defaultdict(list)
    cols = defaultdict(list)
    squares = defaultdict(list)

    for r, v in enumerate(board):
        for c, val in enumerate(v):
            if val == '.':
                continue
            if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):
                return False
            rows[r].append(board[r][c])
            cols[c].append(board[r][c])
            squares[(r//3, c//3)].append(board[r][c])
    
    return True

def isValidSudoku(board):
    res = []
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element != '.':
                res += [(i, element), (element, j), (i // 3, j // 3, element)]
    return len(res) == len(set(res))

if __name__ == "__main__":
    st = time.process_time()
    res = sudoku_checker(board)
    # res = isValidSudoku(board)
    print(res)
    et = time.process_time()
    tt = et - st
    print('CPU Execution time:', tt, 'seconds')

