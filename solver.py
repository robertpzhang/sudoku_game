"""
The solver python file contains the sudoku board game class

Author: Robert Zhang
02/22/2020
"""
import copy

class sudoku_board():
    def __init__(self, board):
        self.board = board
        self.start_board = copy.deepcopy(board)

    def reset(self):
        self.board = copy.deepcopy(self.start_board)

    def find_empty(self):
        row = len(self.board)
        col = len(self.board[0])
        for i in range(row):
            for j in range(col):
                if self.board[i][j] == 0:
                    return [i, j]
        # everything is filled
        # sudoku is solved
        return [-1, -1]

    def solve_sudoku(self):
        # index count for the current filler
        [row, col] = self.find_empty()
        if row == -1 and col == -1:
            # Sudoku is solved
            return True

        for i in range(1, 10):
            self.board[row][col] = i
            if not self.valid():
                self.board[row][col] = 0
                continue
            if self.solve_sudoku():
                return True
            else:
                self.board[row][col] = 0

        return False

    def row_valid(self):
        """
        row_valid checks every row in self.board to see if there is redundant element in the row
        0 is not checked as the matrix is initialized with 0 elements

        :param self.board: 2D matrix
        :return: true or false if the rows are valid

        """
        row = len(self.board)
        col = len(self.board[0])
        for i in range(row):
            hash_set = set()
            for j in range(col):
                if self.board[i][j] != 0 and self.board[i][j] in hash_set:
                    return False
                else:
                    hash_set.add(self.board[i][j])
            # hash_set.clear()
        return True

    def col_valid(self):
        """
        col_valid checks every col in self.board to see if there is redundant element in the col
        0 is not checked as the matrix is initialized with 0 elements
        :param self.board: 2D matrix (numpy)
        :return: True or false if the cols are valid
        """

        row = len(self.board)
        col = len(self.board[0])
        for j in range(col):
            hash_set = set()
            for i in range(row):
                if self.board[i][j] != 0 and self.board[i][j] in hash_set:
                    return False
                else:
                    hash_set.add(self.board[i][j])
            # hash_set.clear()

        return True

    def grid_valid(self):
        """
        grid_valid checks every grid in self.board to see if there is redundant element in the grid
        0 is not checked as the matrix is initialized with 0 elements

        :param self.board: 2D matrix [[0 0 0] [0 0 0]] ... etc
        :return: True of False if the grid is valid
        """
        for i in range(3):
            for s in range(3):
                hash_set = set()
                for j in range(3):
                    for k in range(3):
                        if self.board[i * 3 + j][s * 3 + k] != 0 and self.board[i * 3 + j][s * 3 + k] in hash_set:
                            return False
                        else:
                            hash_set.add(self.board[i * 3 + j][s * 3 + k])
                # hash_set.clear()
        return True

    def valid(self):
        """
        valid method calls grid valid, row valid, and column valid method
        to check if the self.board solution is accurate right now
        :param self.board: 2D matrix of the self.board
        :return: True or False if the grid is valid

        """
        return self.grid_valid() and self.row_valid() and self.col_valid()

