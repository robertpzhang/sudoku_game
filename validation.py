"""
 The validation class to validate the current solution of the sudoku board
 Author: Robert Zhang
 02/22/2020

"""

def row_valid(board):
    """
    row_valid checks every row in board to see if there is redundant element in the row
    0 is not checked as the matrix is initialized with 0 elements

    :param board: 2D matrix
    :return: true or false if the rows are valid

    """
    row = len(board)
    col = len(board[0])
    for i in range(row):
        hash_set = set()
        for j in range(col):
            if board[i][j] != 0 and board[i][j] in hash_set:
                return False
            else:
                hash_set.add(board[i][j])
        hash_set.clear()
    return True


def col_valid(board):
    """
    col_valid checks every col in board to see if there is redundant element in the col
    0 is not checked as the matrix is initialized with 0 elements
    :param board: 2D matrix (numpy)
    :return: True or false if the cols are valid
    """

    row = len(board)
    col = len(board[0])
    for j in range(col):
        hash_set = set()
        for i in range(row):
            if board[i][j] != 0 and board[i][j] in hash_set:
                return False
            else:
                hash_set.add(board[i][j])
        hash_set.clear()

    return True


def grid_valid(board):
    """
    grid_valid checks every grid in board to see if there is redundant element in the grid
    0 is not checked as the matrix is initialized with 0 elements

    :param board: 2D matrix [[0 0 0] [0 0 0]] ... etc
    :return: True of False if the grid is valid
    """

    for i in range(3):
        for s in range(3):
            hash_set = set()
            for j in range(3):
                for k in range(3):
                    if board[i * 3 + j][s * 3 + k] != 0 and board[i * 3 + j][s * 3 + k] in hash_set:
                        return False
                    else:
                        hash_set.add(board[i * 3 + j][s * 3 + k])
            hash_set.clear()
    return True


def valid(board):
    """
    valid method calls grid valid, row valid, and column valid method
    to check if the board solution is accurate right now
    :param board: 2D matrix of the board
    :return: True or False if the grid is valid

    """
    return grid_valid(board) and row_valid(board) and col_valid(board)
