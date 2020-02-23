"""
Solver file contains the function so correctly solve the sudoku

Author: Robert Zhang
02/22/2020
"""
from validation import valid


def find_empty(board):
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] == 0:
                return [i, j]
    # everything is filled
    # sudoku is solved
    return [-1, -1]


def solve_sudoku(board):
    # index count for the current filler
    [row, col] = find_empty(board)
    if row == -1 and col == -1:
        # Sudoku is solved
        return True

    for i in range(1, 10):
        board[row][col] = i
        if not valid(board):
            board[row][col] = 0
            continue
        if solve_sudoku(board):
            return True
        else:
            board[row][col] = 0

    return False

