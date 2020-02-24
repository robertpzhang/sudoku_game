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
    game = 3;
    window = tkinter.Tk()
    sudoku_gui(window, game)
    window.mainloop()

    # creating a 2D array for the grid
    grid =[[0 for x in range(9) ]for y in range(9)]

    # assigning values to the grid
    grid= [[3,0,6,5,0,8,4,0,0],
          [5,2,0,0,0,0,0,0,0],
          [0,8,7,0,0,0,0,3,1],
          [0,0,3,0,1,0,0,8,0],
          [9,0,0,8,6,3,0,0,5],
          [0,5,0,0,9,0,6,0,0],
          [1,3,0,0,0,0,2,5,0],
          [0,0,0,0,0,0,0,7,4],
          [0,0,5,2,0,6,3,0,0]]

    game = sudoku_board(grid)

    start = time.perf_counter()
    print(game.valid())
    if game.solve_sudoku():
        print("valid solution")
        print(np.array(grid))
    else:
        print(grid)
        print("Invalid board! No solution")

    t = time.perf_counter() - start
    print(t)
    # if success print the grid
    # if(solve_sudoku(grid)):
    #     print_grid(grid)
    # else:
    #     print "No solution exists"