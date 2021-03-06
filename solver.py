"""
The solver python file contains the sudoku board game class

Author: Robert Zhang
02/22/2020
"""
import copy
import random


class sudoku_board():
    """
    The sudoku class board that has functioanlities of solve, valid and a board (2D matrix)
    """
    def __init__(self):
        """
        Constructor method that randonly generates a 2D board game of sudoku
        """
        self.board = [[0 for x in range(9)] for y in range(9)]
        self.generate_random()
        self.start_board = copy.deepcopy(self.board)

    def reset(self):
        """
        Reset method resets the current (insolving) to the original generated board
        :return: sets the original board
        """
        self.board = copy.deepcopy(self.start_board)

    def find_empty(self):
        """
        Find the first empty index
        :return: [row col] index of the first 0 in the board
        """
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
        """
        The solve sudoku method solves the sudoku game
        :return: True if the solve is success, false if not
        """
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

    def ran_gen(self):
        """
        Utilizes a random algorithm to generate a random 2D matrix of board game
        :return: True or False
        """
        # index count for the current filler
        [row, col] = self.find_empty()
        if row == -1 and col == -1:
            # Sudoku is solved
            return True
        x = [i for i in range(9)]
        random.shuffle(x)
        for i in x:
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
        for i in range(9):
            hash_set = set()
            for j in range(9):
                if self.board[i][j] != 0 and self.board[i][j] in hash_set:
                    return False
                else:
                    hash_set.add(self.board[i][j])
            hash_set.clear()
        return True

    def col_valid(self):
        """
        col_valid checks every col in self.board to see if there is redundant element in the col
        0 is not checked as the matrix is initialized with 0 elements
        :param self.board: 2D matrix (numpy)
        :return: True or false if the cols are valid
        """

        for j in range(9):
            hash_set = set()
            for i in range(9):
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

    def generate_random(self):
        """
        The method generates a random sudoku game that is solvable

        :return: a randomly generated 2D matrix of sudoku game
        """
        # generates a random value 1-9
        self.ran_gen()
        for i in range(56):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while self.board[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            self.board[row][col] = 0
