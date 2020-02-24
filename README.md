# Sudoku Game
Author: Robert Zhang 

Date: 02/22/2020 

The sudoku program randomly initializes a random sudoku game that is 100% solvable, displays a GUI interface for the user to solve the sudoku game. If the user cannot solve the sudoku, the user can call the solver helper to help solve the sudoku.

The sudoku program utilizes object-oriented programing principles and data structure & algorithms for implementation of the solver and generator methods.

<img src="gui_demo.png" width="400" height="500">

## Prerequisite
### Tools:
- Python 3
### Library:
- Tkinter

## Installation
```
git clone https://github.com/robertpzhang/sudoku_game
cd sudoku_game
python main.py
```

## Functionalities

- Generate a newly random Sudoku game
  - The generator algorithm starts the grid with a blank 9x9 matrix
  - The generator generated a random set of numbers to fill in
  - The generator utilizes the trial and error backtrack to try to solve the blank matrix
  - The generator then removes 55 slots in the matrix
  
- Solve and validate a solution based on trial and error and backtracking algorithm
  - The solver finds the first empty slot in the matrix
  - The solver fills in numbers starting from 1 - 9
  - The solver validates if the number made the matrix valid 
  - If valid, the solver goes to the next empty slot; if not valid, the solver backtracks to the last slot.
