"""
Main Program to run the Sudoku game with the GUI part

Author: Robert Zhang
02/22/2020
"""

from solver import sudoku_board
import numpy as np
import time, random
import tkinter
from sudoku_gui import sudoku_gui


if __name__ == "__main__":
    """
    The main program that calls the GUI and backend of the program
    """
    # creating a 2D array for the grid
    game = sudoku_board()
    window = tkinter.Tk()
    sudoku_gui(window, game)
    window.mainloop()
