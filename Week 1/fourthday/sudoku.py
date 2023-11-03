# Sudoku solver
import time
t1 = time.time()
def solveSudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for k in range(1, 10):
                    board[i][j] = str(k)
                    if isValidSudoku(board):
                        if solveSudoku(board):
                            return True
                    board[i][j] = '.'
                return False
    return True

def isValidSudoku(board):
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            if board[i][j] != '.':
                row.append(board[i][j])
            if board[j][i] != '.':
                col.append(board[j][i])
        if len(row) != len(set(row)) or len(col) != len(set(col)):
            return False
    for i in range(3):
        for j in range(3):
            box = []
            for k in range(3):
                for l in range(3):
                    if board[i*3+k][j*3+l] != '.':
                        box.append(board[i*3+k][j*3+l])
            if len(box) != len(set(box)):
                return False
    return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# Print the solved  sudoku board

def print_board(solved_board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()
        
solved_board = solveSudoku(board)
print_board(board)
t2 = time.time()
print("The time taken is:", t2-t1)






    
